from bs4 import BeautifulSoup
import requests

def send_msg(session, msg):
    url = "https://chat.danwin1210.me/chat.php?action=post&session="+session+"&lang=en"

    header = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'
    }
    proxy = {
    'http' : "socks5://127.0.0.1:9150",
    'https' : "socks5://127.0.0.1:9150"
    }

    formmsg = []

    page = requests.get(url, proxies=proxy, headers=header)
    soup = BeautifulSoup(page.content, 'lxml')
    form_msg=soup.find("form", action="/chat.php",enctype="multipart/form-data", method="post")
    for info in form_msg.find_all("input", type="hidden"):
          #print(info)
          info = info.__str__()
          info = info.split("\"")
          formmsg += [info[5]]

    #print(formmsg)

    data = {}
    data.update({'lang': 'en'})
    data.update({'nc': formmsg[1]})
    data.update({'action': 'post'})
    data.update({'session': formmsg[3]})
    data.update({'postid': formmsg[4]})
    data.update({'message': msg})
    data.update({'sendto': "s *"})

    requests.post(url, data=data, proxies=proxy, headers=header)
    
    #<option selected="" value="s *">-All chatters-</option>
    #<option value="s ?">-Members only-</option>
    #<option value="s %">-Staff only-</option>
    #<option value="s _">-Admin
