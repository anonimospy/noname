from bs4 import BeautifulSoup
import requests


def setup_login():
    url = "https://chat.danwin1210.me/chat.php"

    header = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Connection': 'keep-alive'
    }
    proxy = {
        'http': "socks5://127.0.0.1:9150",
        'https': "socks5://127.0.0.1:9150"
    }

    formmsg = []
    session = ""

    keep = requests.Session()
    page = keep.get(url, proxies=proxy, headers=header)
    soup = BeautifulSoup(page.content, 'lxml')
    # form_msg=soup.find("form", action="/chat.php",enctype="multipart/form-data", method="post")
    for info in soup.find_all("input", type="hidden"):
        info = info.__str__()
        info = info.split("\"")
        formmsg += [info[5]]

    captcha = soup.find("img", alt="")
    challeng = soup.find_all("input", type="hidden")
    print(captcha)
    captcha_s = input("captcha: ")

    data = {}
    data.update({'lang': 'en'})
    data.update({'nc': formmsg[1]})
    data.update({'action': formmsg[2]})
    data.update({'nick': 'anonimosBot'})
    data.update({'pass': 'blabla123'})
    data.update({'challenge': formmsg[3]})
    data.update({'captcha': captcha_s})
    # there is also a hidden challenge
    # another nc thing going on aswell
    # print(data)

    sent = keep.post(url, data=data, proxies=proxy, headers=header)
    page = keep.get(url, proxies=proxy, headers=header)
    soup = BeautifulSoup(page.content, 'lxml')
    for info in soup.find_all("input", type="hidden"):
        info = info.__str__()
        info = info.split("\"")
        # print(info)
        if len(info[5]) > 13:
            session = info[5]
            print(session)

            # form_msg += [info]

    return session

