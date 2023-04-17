import requests


def get_sites_server(*args):
    print("URL\t\t\tServer")
    print("-------------------------------------")
    for site in args:
        r = requests.get(site)
        result = r.headers
        print(f'{r.url}\t{result["Server"]}')


get_sites_server(
    "https://vk.com",
    "http://sudexperts.ru",
    "http://15min.lt",
    "http://bash.org",
    "http://rutracker.org",
)
