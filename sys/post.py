import json
import requests

if __name__ == "__main__":

    url = "http://127.0.0.1:8000/query"
    query_result = []
    with open("./solved_query.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            if line and line[0] != "#":
                response = requests.post(url = url, json = {"query": line})
                query_result += [(line, response.text)]
    with open("./query_results.txt", "w", encoding="utf8") as f:
        for i, (line, res) in enumerate(query_result):
            if res.startswith("<"):
                res = "Error"
            f.write(f"query {i+1}:{line}:\n{res}\n")
