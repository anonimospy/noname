from loginsc import setup_login
from sendmsg import send_msg
from readchat import read_chat

from inputimeout import inputimeout, TimeoutOccurred

import sys

test = 0


# works
def readmsg(session):
    global test
    test =0 
    hit = True
    last_msg = ""
    while True:
        hit, last_msg, msg_log = read_chat(hit, last_msg, session)
        if msg_log != "":
            print(msg_log)
            # f = open('log.txt', 'a+')
            # f.write(msg_log)
            # f.close()
        while test == 0 :
            print("Fuckkkk")
            read_start()


# wroks
# setup_login()
session = setup_login()


def read_start():
    global test
    try:
        test = 0
        something = inputimeout(prompt='Enter msg: ', timeout=5)

        while True:
            user_input = something
            send_msg(session, user_input)
            readmsg(session)

    except TimeoutOccurred:
        test = 1  
        readmsg(session)


readmsg(session)

