from bs4 import BeautifulSoup
from urllib.request import urlopen
import telepot
#import os

access_token = '1336751738:AAGYLFLDIzXARTkti1KuhmQPizrGDbph0oM'
#os.environ["BOT_TOKEN"]
mc = '1141765178'
bot = telepot.Bot(token)

def handle(msg):
    with urlopen('https://www.jbnu.ac.kr/kor/?menuID=139&pno=1') as response:
        soup = BeautifulSoup(response, 'html.parser')
        i = 1
        for anchor in soup.select('a[href^="?menuID=139&pno=1&mode=view&no="]'):
            announcement = anchor.get_text(strip=True)
            if not announcement.find(msg['text']) == -1:
                data = '[' + str(i) + '] ' + announcement
                print(data)
                bot = telepot.Bot(access_token)
                bot.sendMessage(msg['from']['id'], data)
                i = i + 1
bot.message_loop(handle)

while True:
    pass
