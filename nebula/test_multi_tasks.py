import random
import time
import json

from nebula3.gclient.net import ConnectionPool

from nebula3.Config import Config
from nebula3.common import *
from FormatResp import print_resp
import threading


def search():
    st = time.time()
    # search_num = random.randint(5, 8)
    search_num=9
    client = None
    try:
        client = connection_pool.get_session('root', 'nebula')
        assert client is not None

        url = "USE stockKGQA;"

        if search_num == 1:
            # 单表查询
            url += "match (n:stock) where n.stock.name=='stock_name_0' return n"
        elif search_num == 2:
            # 单表多实体比较查询
            url += "match (s:stock)-[e:has_stock_latest_data]->(h:stock_data) where s.stock.name == 'stock_name_0' and h.stock_data.stock_data_date == date('2023-08-02') with h.stock_data.closing_price as temp match (s:stock)-[e:has_stock_latest_data]->(h:stock_data) where s.stock.name == 'stock_name_1000' and h.stock_data.stock_data_date == date('2023-08-02') return abs(h.stock_data.closing_price - temp);"
        elif search_num == 3:
            # 单表多实体联合查询
            url += "match (s:stock)-[e:has_stock_latest_data]->(h:stock_data) where s.stock.name == 'stock_name_0' and h.stock_data.stock_data_date == date('2023-08-02')  return h.stock_data.closing_price  union match (s:stock)-[e:has_stock_latest_data]->(h:stock_data) where s.stock.name == 'stock_name_1000' and h.stock_data.stock_data_date == date('2023-08-02')  return h.stock_data.closing_price;"
        elif search_num == 4:
            # 单跳查询
            # url += "match (s:stock)-->(i1:industry), (s:stock)-->(i2:industry) where i1.industry.name=='industry_name_2' and i2.industry.name=='industry_name_5002' return s.stock.name;"
            url += "match (s:stock)-[e:has_stock_latest_data]->(h:stock_data) where s.stock.name=='stock_name_0' return h.stock_data.closing_price;"
        elif search_num == 5:
            # 两跳查询
            url += "match (i:industry)<--(s:stock)<--(sh:stockholder) where sh.stockholder.name == 'stockholder_name_0' and i.industry.name == 'industry_name_0' return s.stock.name;"
            # url += "match (sh:stockholder)-->(s:stock), (n:stock_data) where sh.stockholder.name=='stockholder_name_0' and s.stock.name==n.stock_data_name and n.stock_data_name contains 'stock_latest_data_name' return n"
        elif search_num == 6:
            # 三跳查询
            # url += "match (sh:stockholder)-[h:is_stockholder_of]->(s:stock), (s:stock)-->(i1:industry)-->(i2:industry) where sh.stockholder.name == 'stockholder_name_0' and h.shareholding_ratio < 30 return s.stock.name as name, i1.industry.name as current_industry, i2.industry.name as downstream_industries;"
            # url += "go from 'stockholder_0' over is_stockholder_of where properties(edge).shareholding_ratio < 30 YIELD dst(edge) as dstid | go from $-.dstid over associate yield dst(edge) AS destination1 | go from $-.destination1 over affect yield $-.destination1, dst(edge) AS destination2;"
            shname = 'stockholder_name_' + str(random.randint(0,10000))
            url += "match (sh:stockholder)-[h:is_stockholder_of]->(s:stock) where sh.stockholder.name == '{}' and h.shareholding_ratio < 30 with s match (s:stock)-->(i1:industry)-->(i2:industry) return s.stock.name as name, i1.industry.name as current_industry, i2.industry.name as downstream_industries;".format(shname)
        elif search_num == 7:
            # 四跳查询
            url += "match (m:fund_manager)-->(f:public_offering_fund)-->(s:stock)-->(i1:industry)-->(i2:industry) where m.fund_manager.name == 'fund_manager_name_0' return i1.industry.name, i2.industry.name"
        elif search_num == 8:
            # 两跳查询+查询更新表
            url += "match (sh:stockholder)-->(s:stock)-[e:has_stock_latest_data]->(n:stock_data) where sh.stockholder.name=='stockholder_name_1' return s.stock.name, n.stock_data.closing_price;"
        elif search_num == 9:
            random_name = "stock_name_" + str(random.randint(0,5000))
            url += "match (s:stock)-->(sd:stock_data) where s.stock.name == '{}' and date('2023-08-02') - sd.stock_data.stock_data_date <= 3 return avg(sd.stock_data.opening_price)".format(random_name)

        resp = client.execute(url)
        assert resp.is_succeeded(), resp.error_msg()


    except Exception as x:
        print(x)
        import traceback

        print(traceback.format_exc())
    finally:
        if client is not None:
            client.release()

    print("search time: ", time.time() - st)
    thread_search_cur = threading.Timer(random.uniform(0, 1), search)
    # thread_search_cur=threading.Timer(3, search)
    thread_search_cur.start()


def update_thread(start, end, updateData, updateTag):
    client = None
    try:
        # print("solving from ", start, " to ", end, ": ")

        client = connection_pool.get_session('root', 'nebula')
        assert client is not None

        # st = time.time()
        url = "USE stockKGQA;"
        for i in range(start, end):
            id = "stock_latest_data_" + str(i)
            name = updateData[i]["name"]
            stock_data_date = str(updateData[i]["stock_data_date"])
            opening_price = str(updateData[i]["opening_price"])
            closing_price = str(updateData[i]["closing_price"])
            maximum_price = str(updateData[i]["maximum_price"])
            minimum_price = str(updateData[i]["minimum_price"])
            range_ = str(updateData[i]["range"])
            volume = str(updateData[i]["volume"])
            raising_limit_days = str(updateData[i]["raising_limit_days"])
            raising_limit = str(updateData[i]["raising_limit"])
            hong_san_bing = str(updateData[i]["hong_san_bing"])
            url += "UPDATE VERTEX ON " + updateTag + " '" + id + "' SET stock_data_date = date('" + stock_data_date + "'), opening_price = " + opening_price + ", closing_price = " + closing_price + ", maximum_price = " + maximum_price + ", minimum_price = " + minimum_price + ", range = " + range_ + ", volume = " + volume + ", raising_limit_days = " + raising_limit_days + ", raising_limit = " + raising_limit + ", hong_san_bing = " + hong_san_bing + ";"
        resp = client.execute(url)
        assert resp.is_succeeded(), resp.error_msg()
        # print_resp(resp)
        # print(time.time() - st)

        # print("Example finished")

    except Exception as x:
        print(x)
        import traceback

        print(traceback.format_exc())
    finally:
        if client is not None:
            client.release()


# Get the data to be updated
def getUpdateData():
    updateData = []
    for i in range(5000):
        name = "stock_latest_data_name_" + str(i)
        stock_data_date = "2023-08-02"
        opening_price = random.uniform(1, 10)
        closing_price = random.uniform(1, 10)
        maximum_price = random.uniform(1, 10)
        minimum_price = random.uniform(1, 10)
        range_ = random.uniform(1, 10)
        volume = 8
        raising_limit_days = 3
        raising_limit = "TRUE"
        hong_san_bing = "FALSE"
        updateData.append(
            {"name": name, "stock_data_date": stock_data_date, "opening_price": opening_price, "closing_price": closing_price, "maximum_price": maximum_price,
             "minimum_price": minimum_price, "range": range_, "volume": volume, "raising_limit_days": raising_limit_days,
             "raising_limit": raising_limit, "hong_san_bing": hong_san_bing})
    return updateData


def update():
    updateData = getUpdateData()  # get data

    stt = time.time()  # starting time

    # Use multi thread
    threads = list()
    for i in range(0, 10):
        # threads.append(
        #     threading.Thread(target=update_thread,
        #                      kwargs={'start': i * 500, 'end': (i + 1) * 500, 'updateData': updateData, 'updateTag': 'stock_latest_data'},
        #                      name='thread{}'.format(i))
        # )
        threads.append(
            threading.Thread(target=update_thread,
                             kwargs={'start': i * 500, 'end': (i + 1) * 500, 'updateData': updateData, 'updateTag': 'stock_data'},
                             name='thread{}'.format(i))
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print("###################################################################################### update time: ", time.time() - stt)

    thread_update = threading.Timer(3, update)
    thread_update.start()


if __name__ == '__main__':
    config = Config()
    config.max_connection_pool_size = 100

    # init connection pool
    connection_pool = ConnectionPool()

    assert connection_pool.init([('172.23.109.155', 9669)], config)
    # assert connection_pool.init([('192.168.3.46', 9669)], config)

    # thread_update=threading.Timer(3, update)
    # thread_update.start()
    # thread_update.join()
    #
    # threads_search = list()
    # for i in range(0, 10):
    #     threads_search.append(
    #         threading.Timer(2, search)
    #     )
    # for thread in threads_search:
    #     thread.start()
    # for thread in threads_search:
    #     thread.join()

    update()
    # search_threads = list()
    # for i in range(1000):
    #     search()

    # update_thread=threading.Thread(target=update)
    # update_thread.start()
    search_threads = list()
    for i in range(0, 10):
        search_threads.append(
            threading.Thread(target=search)
        )
    for search_thread in search_threads:
        search_thread.start()
    # for search_thread in search_threads:
    #     search_thread.join()

    sttt = time.time()
    while (time.time() - sttt > 10):
        # close connect pool
        connection_pool.close()
