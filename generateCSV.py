import csv
import random
import time
from datetime import timedelta, date, datetime


# stock(code string, name string, chinese_spelling string, registered_capital float, listed_sector string, establishment_date date, province string)
def generate_stock():
    # row = [":VID(string)", "code:string", "name:string", "chinese_spelling:string", "registered_capital:float",
    #        "listed_sector:string", "establishment_date:date", "province:string"]
    # with open('./stockKGQA/stock.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(row)

    predefined_name = ["国泰君安", "中信证券", "东方财富", "同花顺", "比亚迪", "科大讯飞", "华泰证券", "宁德时代"]
    rows = []
    st = time.time()
    for i in range(5000):
        VID = "stock_" + str(i)
        code = "stock_code_" + str(i)
        if i < len(predefined_name):
            name = predefined_name[i]
        else:
            name = "stock_name_" + str(i)
        chinese_spelling = "stock_name_" + str(i)
        registered_capital = random.uniform(100, 1000)
        listed_sector = "创业板"
        establishment_date = "2023-0" + str(random.randint(1, 9)) + "-" + str(random.randint(10, 28))
        province = random.choice(["上海市", "北京市"])
        row = [VID, code, name, chinese_spelling, registered_capital, listed_sector, establishment_date, province]
        rows.append(row)
    
    with open('./stockKGQA/stock.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_stock total: ", time.time() - st)


# stock_data(code string, name string, stock_data_date date, opening_price float, closing_price float,
#                              maximum_price float, minimum_price float, range float, volume int,
#                              raising_limit_days int, raising_limit bool, hong_san_bing bool);
def generate_stock_data():
    st = time.time()
    rows = []
    for i in range(5000):
        for j in range(10):
            for k in range(365):
                VID = "stock_data_" + str(i) + "_" + str(j) + "_" + str(k)
                # code = "stock_code_" + str(i)
                # name = "stock_name_" + str(i)
                stock_data_date = str(date.today() - timedelta(days=k+365*j))
                opening_price = random.uniform(1, 10)
                closing_price = random.uniform(1, 10)
                maximum_price = random.uniform(1, 10)
                minimum_price = random.uniform(1, 10)
                range_ = random.uniform(1, 10)
                volume = random.randint(1, 10)
                raising_limit_days = random.randint(1, 5)
                raising_limit = "TRUE" if random.randint(1, 5) == 1 else "FALSE"
                hong_san_bing = "TRUE" if random.randint(1, 5) == 1 else "FALSE"
                # row = [VID, code, name, stock_data_date, opening_price, closing_price, maximum_price, minimum_price, range_, volume,
                #        raising_limit_days, raising_limit, hong_san_bing]
                row = [VID, stock_data_date, opening_price, closing_price, maximum_price, minimum_price, range_, volume,
                       raising_limit_days, raising_limit, hong_san_bing]
                rows.append(row)
    with open('./stockKGQA/stock_data.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_stock_data total: ", time.time() - st)


# stock_latest_data(code string, name string, stock_data_date date, opening_price float, closing_price float,
#                              maximum_price float, minimum_price float, range float, volume int,
#                              raising_limit_days int, raising_limit bool, hong_san_bing bool);
# def generate_stock_latest_data():
#     st = time.time()
#     for i in range(5000):
#         VID = "stock_latest_data_" + str(i)
#         code = "stock_latest_data_code_" + str(i)
#         name = "stock_latest_data_name_" + str(i)
#         stock_data_date = "2023-08-01"
#         opening_price = random.uniform(1, 10)
#         closing_price = random.uniform(1, 10)
#         maximum_price = random.uniform(1, 10)
#         minimum_price = random.uniform(1, 10)
#         range_ = random.uniform(1, 10)
#         volume = random.randint(1, 10)
#         raising_limit_days = random.randint(1, 5)
#         raising_limit = "TRUE" if random.randint(1, 5) == 1 else "FALSE"
#         hong_san_bing = "TRUE" if random.randint(1, 5) == 1 else "FALSE"
#         row = [VID, code, name, stock_data_date, opening_price, closing_price, maximum_price, minimum_price, range_, volume,
#                raising_limit_days, raising_limit, hong_san_bing]
#         with open('./stockKGQA/stock_latest_data.csv', 'a', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(row)
#     print("generate_stock_latest_data total: ", time.time() - st)


# stock_historical_data(code string, name string, stock_data_date date, opening_price float, closing_price float,
#                                  maximum_price float, minimum_price float, range float, volume int,
#                                  raising_limit_days int, raising_limit bool, hong_san_bing bool);
# def generate_stock_historical_data():
#     st = time.time()
#     for i in range(5000):
#         rows = []
#         for j in range(10):
#             for k in range(365):
#                 VID = "stock_historical_data_" + str(i) + "_" + str(j) + "_" + str(k)
#                 code = "stock_historical_data_code_" + str(i) + "_" + str(j) + "_" + str(k)
#                 name = "stock_historical_data_name_" + str(i) + "_" + str(j) + "_" + str(k)
#                 stock_data_date = "2023-08-01"
#                 opening_price = random.uniform(1, 10)
#                 closing_price = random.uniform(1, 10)
#                 maximum_price = random.uniform(1, 10)
#                 minimum_price = random.uniform(1, 10)
#                 range_ = random.uniform(1, 10)
#                 volume = random.randint(1, 10)
#                 raising_limit_days = random.randint(1, 5)
#                 raising_limit = "TRUE" if random.randint(1, 5) == 1 else "FALSE"
#                 hong_san_bing = "TRUE" if random.randint(1, 5) == 1 else "FALSE"
#                 row = [VID, code, name, stock_data_date, opening_price, closing_price, maximum_price, minimum_price, range_, volume,
#                        raising_limit_days, raising_limit, hong_san_bing]
#                 rows.append(row)
#         with open('./stockKGQA/stock_historical_data.csv', 'a', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerows(rows)
#     print("generate_stock_historical_data total: ", time.time() - st)


# stock_financial_information_quarter(code string, name string, stock_financial_information_date date, year int, quarter int, net_profit float, inventory_turnover float)
def generate_stock_financial_information():
    st = time.time()
    rows = []
    for i in range(5000):  # 5000*10*4
        for j in range(10):
            for k in range(1, 5):
                VID = "stock_financial_information_" + str(i) + "_" + str(j) + "_" + str(k)
                # code = "stock_financial_information_quarter_code_" + str(i) + "_" + str(j) + "_" + str(k)
                # name = "stock_financial_information_quarter_name_" + str(i) + "_" + str(j) + "_" + str(k)
                if k == 1:
                    stock_financial_information_date = str(j) + "-04-01"
                elif k == 2:
                    stock_financial_information_date = str(j) + "-07-01"
                elif k == 3:
                    stock_financial_information_date = str(j) + "-10-01"
                else:
                    stock_financial_information_date = str(j + 1) + "-01-01"
                year = 2013+j
                quarter = k
                net_profit = random.uniform(100, 1000)
                inventory_turnover = random.uniform(10, 50)
                # row = [VID, code, name, stock_financial_information_date, year, quarter, net_profit, inventory_turnover]
                row = [VID, stock_financial_information_date, year, quarter, net_profit, inventory_turnover]
                rows.append(row)
    with open('./stockKGQA/stock_financial_information.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_stock_financial_information total: ", time.time() - st)




# new_stock(code string, amount int, online_release_date string)
def generate_new_stock():
    st = time.time()
    rows = []
    for i in range(5000):
        VID = "new_stock_" + str(i)
        code = "new_stock_code_" + str(i)
        amount = random.randint(10, 100)
        online_release_date = "2011-0" + str(random.randint(1, 9)) + "-" + str(random.randint(10, 28))
        row = [VID, code, amount, online_release_date]
        rows.append(row)
    with open('./stockKGQA/new_stock.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    rows = []
    for i in range(5000, 5100):
        VID = "new_stock_" + str(i)
        code = "new_stock_code_" + str(i)
        amount = random.randint(10, 100)
        online_release_date = "2022-0" + str(random.randint(9, 12)) + "-" + str(random.randint(10, 28))
        row = [VID, code, amount, online_release_date]
        rows.append(row)
    with open('./stockKGQA/new_stock.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_new_stock total: ", time.time() - st)


# chairman(name string, sex string, appointment_date string, departure_date string)
def generate_chairman():
    predefined_name = ["贺青"]
    st = time.time()
    rows = []
    for i in range(5000):
        VID = "chairman_" + str(i)
        if i < len(predefined_name):
            name = predefined_name[i]
        else:
            name = "chairman_name_" + str(i)
        sex = random.choice(["male", "female"])
        appointment_date = str(random.randint(2013, 2022)) + "-0" + str(random.randint(1, 9)) + "-" + str(random.randint(10, 28))
        departure_date = "none"
        row = [VID, name, sex, appointment_date, departure_date]
        rows.append(row)
    with open('./stockKGQA/chairman.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_chairman total: ", time.time() - st)


# stockholder(name string)
def generate_stockholder():
    st = time.time()
    rows = []
    for i in range(100000):
        VID = "stockholder_" + str(i)
        name = "stockholder_name_" + str(i)
        row = [VID, name]
        rows.append(row)
    with open('./stockKGQA/stockholder.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_stockholder total: ", time.time() - st)


# trade(code string, name string)
def generate_trade():
    predefined_name = ["生态园林", "券商"]
    st = time.time()
    rows = []
    for i in range(2000):
        VID = "trade_" + str(i)
        code = "trade_code_" + str(i)
        if i < len(predefined_name):
            name = predefined_name[i]
        else:
            name = "trade_name_" + str(i)
        row = [VID, code, name]
        rows.append(row)
    with open('./stockKGQA/trade.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_trade total: ", time.time() - st)


def generate_trade_data():
    st = time.time()
    rows = []
    for i in range(2000):
        for j in range(10):
            for k in range(365):
                VID = "trade_data_" + str(i) + "_" + str(j) + "_" + str(k)
                # code = "trade_historical_data_code_" + str(i) + "_" + str(j) + "_" + str(k)
                # name = "trade_historical_data_name_" + str(i) + "_" + str(j) + "_" + str(k)
                trade_data_date = str(date.today() - timedelta(days=j*365+k))
                opening_price = random.uniform(1, 10)
                closing_price = random.uniform(1, 10)
                maximum_price = random.uniform(1, 10)
                minimum_price = random.uniform(1, 10)
                range_ = random.uniform(1, 10)
                # row = [VID, code, name, trade_data_date, opening_price, closing_price, maximum_price, minimum_price, range_]
                row = [VID, trade_data_date, opening_price, closing_price, maximum_price, minimum_price, range_]
                rows.append(row)
    with open('./stockKGQA/trade_data.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_trade_data total: ", time.time() - st)

# information(id string, name string)
def generate_information():
    st = time.time()
    rows = []
    for i in range(50000):
        VID = "information_" + str(i)
        id = "information_id_" + str(i)
        name = "information_name_" + str(i)
        row = [VID, id, name]
        rows.append(row)
    with open('./stockKGQA/information.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_information total: ", time.time() - st)


# public_offering_fund(code string, name string, sales_status string, management_fee float, latest_scale float,
#                      subscription_start_time datetime, subscription_end_time datetime, latest_net_worth float)
def generate_public_offering_fund():
    predefined_name = ["易方达蓝筹精选混合", "中欧医疗健康混合c", "社保基金"]
    rows = []
    st = time.time()
    for i in range(50000):
        VID = "public_offering_fund_" + str(i)
        code = "public_offering_fund_code_" + str(i)
        if i < len(predefined_name):
            name = predefined_name[i]
        else:
            name = "public_offering_fund_name_" + str(i)
        sales_status = "on sale"
        management_fee = "0.5"
        latest_scale = random.uniform(1000000, 10000000)
        subscription_start_time = str(random.randint(2013, 2022)) + "-0" + str(random.randint(1, 9)) + "-" + str(random.randint(10, 28)) + "T00:00:00"
        subscription_end_time = "2023-0" + str(random.randint(1, 6)) + "-" + str(random.randint(10, 28)) + "T00:00:00"
        latest_net_worth = random.uniform(2000000, 20000000)
        row = [VID, code, name, sales_status, management_fee, latest_scale, subscription_start_time, subscription_end_time, latest_net_worth]
        rows.append(row)
    with open('./stockKGQA/public_offering_fund.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_public_offering_fund total: ", time.time() - st)


# fund_manager(name string, sex string, degree string)
def generate_fund_manager():
    predefined_name = ["张坤"]
    rows = []
    st = time.time()
    for i in range(50000):
        VID = "fund_manager_" + str(i)
        if i < len(predefined_name):
            name = predefined_name[i]
        else:
            name = "fund_manager_name_" + str(i)
        sex = random.choice(["male", "female"])
        degree = "master"
        row = [VID, name, sex, degree]
        rows.append(row)
    with open('./stockKGQA/fund_manager.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_fund_manager total: ", time.time() - st)


# industry(name string, scale float)
def generate_industry():
    predefined_name = ["锂电池涂布机"]
    rows = []
    st = time.time()
    for i in range(20000):
        VID = "industry_" + str(i)
        if i < len(predefined_name):
            name = predefined_name[i]
        else:
            name = "industry_name_" + str(i)
        scale = random.uniform(10, 100)
        row = [VID, name, scale]
        rows.append(row)
    with open('./stockKGQA/industry.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_industry total: ", time.time() - st)


##############################################################################################################################################################
# generate edges csv

# originate_from(marketing_time date)
def generate_originate_from():
    st = time.time()
    rows = []
    for i in range(5000):
        srcVID = "stock_" + str(i)
        dstVID = "new_stock_" + str(i)
        marketing_time = "2013-0" + str(random.randint(1, 9)) + "-" + str(random.randint(10, 28))
        row = [srcVID, dstVID, marketing_time]
        rows.append(row)
    with open('./stockKGQA/originate_from.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_originate_from total: ", time.time() - st)


# is_chairman_of()
def generate_is_chairman_of():
    st = time.time()
    rows = []
    for i in range(5000):
        srcVID = "chairman_" + str(i)
        dstVID = "stock_" + str(i)
        row = [srcVID, dstVID]
        rows.append(row)
    with open('./stockKGQA/is_chairman_of.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_is_chairman_of total: ", time.time() - st)


# is_stockholder_of(shareholding_ratio float, circulation_shareholding_ratio float)
def generate_is_stockholder_of():
    rows = []
    st = time.time()
    for i in range(100000):
        srcVID = "stockholder_" + str(i)
        dstVID = "stock_" + str(i % 5000)
        shareholding_ratio = random.uniform(10, 30)
        circulation_shareholding_ratio = random.uniform(10, 30)
        row = [srcVID, dstVID, shareholding_ratio, circulation_shareholding_ratio]
        rows.append(row)
    with open('./stockKGQA/is_stockholder_of.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_is_stockholder_of total: ", time.time() - st)


# belong_to()
def generate_belong_to():
    rows = []
    st = time.time()
    for i in range(5000):
        srcVID = "stock_" + str(i)
        dstVID = "trade_" + str(i % 2000)
        row = [srcVID, dstVID]
        rows.append(row)
    with open('./stockKGQA/belong_to.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_belong_to total: ", time.time() - st)


# hold(position_ratio float, position_amount float)
def generate_hold():
    rows = []
    st = time.time()
    for i in range(50000):
        srcVID = "public_offering_fund_" + str(i)
        dstVID = "stock_" + str(i % 5000)
        position_ratio = random.uniform(10, 30)
        position_amount = random.uniform(1000000, 10000000)
        row = [srcVID, dstVID, position_ratio, position_amount]
        rows.append(row)
    with open('./stockKGQA/hold.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_hold total: ", time.time() - st)


# manage()
def generate_manage():
    rows = []
    st = time.time()
    for i in range(50000):
        srcVID = "fund_manager_" + str(i)
        dstVID = "public_offering_fund_" + str(i)
        row = [srcVID, dstVID]
        rows.append(row)
    with open('./stockKGQA/manage.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_manage total: ", time.time() - st)


# involve(tendency int)
def generate_invovle_stock():
    rows = []
    st = time.time()
    for i in range(50000):
        srcVID = "stock_" + str(i % 5000)
        dstVID = "information_" + str(i)
        tendency = random.choice([-1, 0, 1])
        row = [srcVID, dstVID, tendency]
        rows.append(row)
    with open('./stockKGQA/involve_stock.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_involve_stock total: ", time.time() - st)


# involve(tendency int)
def generate_involve_public_offering_fund():
    rows = []
    st = time.time()
    for i in range(50000):
        srcVID = "public_offering_fund_" + str(i)
        dstVID = "information_" + str(i)
        tendency = random.choice([-1, 0, 1])
        row = [srcVID, dstVID, tendency]
        rows.append(row)
    with open('./stockKGQA/involve_public_offering_fund.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_involve_public_offering_fund total: ", time.time() - st)


# associate()
def generate_associate():
    rows = []
    st = time.time()
    for i in range(20000):
        srcVID = "stock_" + str(i % 5000)
        dstVID = "industry_" + str(i)
        row = [srcVID, dstVID]
        rows.append(row)
    with open('./stockKGQA/associate.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_associate total: ", time.time() - st)


# affect()
def generate_affect():
    rows = []
    st = time.time()
    for i in range(5000):
        for j in range(3):
            srcVID = "industry_" + str(5000 * j + i)
            dstVID = "industry_" + str(5000 * (j + 1) + i)
            row = [srcVID, dstVID]
            rows.append(row)
    with open('./stockKGQA/affect.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_affect total: ", time.time() - st)

# has_stock_data()
def generate_has_stock_data():
    st = time.time()
    rows = []
    for i in range(5000):
        for j in range(10):
            for k in range(365):
                srcVID = "stock_" + str(i)
                dstVID = "stock_data_" + str(i) + "_" + str(j) + "_" + str(k)
                row = [srcVID, dstVID]
                rows.append(row)
    with open('./stockKGQA/has_stock_data.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_has_stock_data total: ", time.time() - st)

# has_stock_financial_information()
def generate_has_stock_financial_information():
    rows = []
    st = time.time()
    for i in range(5000):
        for j in range(10):
            for k in range(1,5):
                srcVID = "stock_" + str(i)
                dstVID = "stock_financial_information_" + str(i) + "_" + str(j) + "_" + str(k)
                row = [srcVID, dstVID]
                rows.append(row)
    with open('./stockKGQA/has_stock_financial_information.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_has_stock_financial_information total: ", time.time() - st)


# has_trade_data()
def generate_has_trade_data():
    rows = []
    st = time.time()
    for i in range(5000):
        for j in range(10):
            for k in range(365):
                srcVID = "trade_" + str(i)
                dstVID = "trade_data_" + str(i) + "_" + str(j) + "_" + str(k)
                row = [srcVID, dstVID]
                rows.append(row)
    with open('./stockKGQA/has_trade_data.csv', 'a+', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("generate_has_trade_data total: ", time.time() - st)


if __name__ == '__main__':
    generate_stock()
    generate_stock_data()
    generate_stock_financial_information()
    generate_new_stock()
    generate_chairman()
    generate_stockholder()
    generate_trade()
    generate_trade_data()
    generate_information()
    generate_public_offering_fund()
    generate_fund_manager()
    generate_industry()

    generate_originate_from()
    generate_is_chairman_of()
    generate_is_stockholder_of()
    generate_belong_to()
    generate_hold()
    generate_manage()
    generate_invovle_stock()
    generate_involve_public_offering_fund()
    generate_associate()
    generate_affect()
    generate_has_stock_data()
    generate_has_stock_financial_information()
    generate_has_trade_data()
