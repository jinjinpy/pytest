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
        bot = telepot.Bot('1336751738:AAGYLFLDIzXARTkti1KuhmQPizrGDbph0oM')
        bot.sendMessage(1141765178, data)
        i += 1
