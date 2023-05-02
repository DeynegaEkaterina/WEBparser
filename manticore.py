import manticoresearch

config = manticoresearch.Configuration(
    host="http://127.0.0.1:9308"
)

client = manticoresearch.ApiClient(config)

indexApi = manticoresearch.IndexApi(client)
searchApi = manticoresearch.SearchApi(client)
utilsApi = manticoresearch.UtilsApi(client)

utilsApi.sql('create table alpindustria(title text, price text, reviews text, description text)')


def search():
    data = searchApi.search({"index": "alpindustria"})
    print(data)


def push(title, price, reviews, description):
    indexApi.insert({"index": "alpindustria", "doc": {"title": f"{title}", "price": f"{price}", "reviews": f"{reviews}", "description": f"{description}"}})

    print("[MANTICORE INFO] Successfully pushed in manticore!")
