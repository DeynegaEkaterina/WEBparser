import requests


def push(document: dict, index: str = "alpindustria", host: str = "localhost", port: int = 9308):
    with requests.Session() as session:
        with session.post(url=f"http://{host}:{port}/insert", json={"index": index, "doc": document}, headers={"Content-Type": "application/json"}) as resp:
            if resp.status_code != 200:
                raise RuntimeError("Error while inserting doc: manticore is not available")

            print(resp.json())
            data = search(query={
                "match": {
                    "description": document["description"]
                    }
                })
            print(f"MANTICORE PUSH {data=}")

            with open("data.txt", "a", encoding="utf-8") as file:
                for i in data['hits']['hits'][0]['_source'].values():
                    file.write(f"{i}\n")

            return resp.json()
        

def search(query: dict, index: str = "alpindustria", host: str = "localhost", port: int = 9308):
    with requests.Session() as session:
        with session.post(url=f"http://{host}:{port}/search", json={
            "index": index, "query": query
        }, headers={"Content-Type": "application/json"}) as resp:
            if resp.status_code != 200:
                raise RuntimeError("Error while inserting doc: manticore is not available")

            return resp.json()


def write_error(data: dict, index: str = "errors", host: str = "localhost", port: int = 9308):
     with requests.Session() as session:
        with session.post(url=f"http://{host}:{port}/insert", json={"index": index, "doc": data}, headers={"Content-Type": "application/json"}) as resp:
            if resp.status_code != 200:
                raise RuntimeError("Error while inserting doc: manticore is not available")
            else:
                print("Error pushed!")
