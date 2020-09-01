#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen
import telepot

with urlopen('https://www.jbnu.ac.kr/kor/?menuID=139&pno=1') as response:
    soup = BeautifulSoup(response, 'html.parser')
    i = 1
    for anchor in soup.select('a[href^="?menuID=139&pno=1&mode=view&no="]'):
        announcement = anchor.get_text(strip=True)
        data = '[' + str(i) + '] ' + announcement
        print(data)
        bot = telepot.Bot('1161290144:AAFmL2S19FhgaQYzsD0QiovTSpW6E21tzxo')
        bot.sendMessage(1141765178, data)
        i += 1
                          
                          
        


"""
import telegram

bot = telegram.Bot('1161290144:AAFmL2S19FhgaQYzsD0QiovTSpW6E21tzxo')
bot.send_message('@jbnuannouncement', 'My first test message')
내계정 아이디 : 1141765178 (getupdates)
"""

"""
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
"""
