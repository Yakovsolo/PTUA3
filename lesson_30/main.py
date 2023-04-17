import requests

# response = requests.get("http://google.com")
# print(response.text)

# r = requests.get("https://www.python.org/static/img/python-logo.png")
# print(r.content)
# b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01"\x00\x00\x00R\x08\x06\x00\x00\x00\xf0\xeb\xd9\xc3\x00\x00\x00\tpHYs\x00\x00\x0b\x13......

# with open("logo.png", "wb") as f:
#     f.write(r.content)

# r = requests.get("https://vk.com/izgoichik")
# print(r.headers)
# print(r.text)
# print(r.content)
# {'Connection': 'keep-alive', 'Content-Length': '48981', 'Server': 'nginx', 'Content-Type': 'text/html; charset=utf-8',
# 'X-Frame-Options': 'DENY', 'Via': '1.1 vegur, 1.1 varnish, 1.1 varnish', 'Accept-Ranges': 'bytes',
# 'Date': 'Sun, 29 Dec 2019 10:30:44 GMT', 'Age': '1447', 'X-Served-By': 'cache-iad2131-IAD, cache-bma1647-BMA',
# 'X-Cache': 'HIT, HIT', 'X-Cache-Hits': '1, 8', 'X-Timer': 'S1577615444.011509,VS0,VE0', 'Vary': 'Cookie',
# 'Strict-Transport-Security': 'max-age=63072000; includeSubDomains'}

# payload = {"q": "pep", "page": "2"}
# r = requests.get("https://www.python.org/search/", params=payload)
# print(r.url)
# # https://www.python.org/search/?q=pep&page=2
# r = requests.get("http://httpbin.org/ip")
# print(r.text)
# {
#   "origin": "78.63.103.114, 78.63.103.114"
# }
