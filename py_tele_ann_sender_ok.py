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
        bot = telepot.Bot('1260153931:AAFr3M2fTUIhRJDSj82nnw-3vfhwQ0fPNpE')
        bot.sendMessage(1141765178, data)
        i += 1
