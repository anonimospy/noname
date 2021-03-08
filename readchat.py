# -*- coding: utf-8 -*-
auther = "The Gay Hentai Cadaver"
from bs4 import BeautifulSoup
import requests
import time

def read_chat(hit, last_msg, session):
    msg_log = ""

    url = "https://danwin1210.me/chat.php?action=view&session="+session+"&lang=en"

    header = {
          'User-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'
    }
    proxy = {
        'http' : "socks5://127.0.0.1:9150",
        'https' : "socks5://127.0.0.1:9150"
    }

    page = requests.get(url,proxies=proxy, headers=header)
    soup = BeautifulSoup(page.content, 'lxml')
    for x in soup.find_all('div',class_="msg")[::-1]:
        msg = x.get_text()
        if last_msg == msg:
            hit = True
            pass
        elif hit == True:
             msg_log += msg+"\n"

    last_msg = msg
    hit = False

    return hit, last_msg, msg_log
