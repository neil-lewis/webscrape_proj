from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import keys2
from twilio.rest import Client

url = 'https://crypto.com/price'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)
print('\n')

rows = soup.findAll('tr')

for row in rows[1:6]:
    td = row.findAll('td')
    if td:
        name = td[2].text
        current_price = td[3].text
        current_price1 = current_price.split('$')
        current_price2 = current_price1[1]
        change = td[3].text


        if '+' in change:
            change = change.split('+')
            change = '+' + change[1]
        else:
            change = change.split('-')
            change = '-' + change[1]

        
        current_price3 = current_price2.lstrip('$')
        current_price3 = current_price3.replace(',','')
        current_price3 = float(current_price3)


        if '+' in change:
            old_price = change.rstrip('%')
            old_price = old_price.lstrip('+')
            old_price = float(old_price) / 100
            old_price = 1 - old_price
            old_price = old_price * float(current_price3)
        
        if '-' in change:
            old_price = change.rstrip('%')
            old_price = old_price.lstrip('-')
            old_price = float(old_price) / 100
            old_price = 1 + old_price
            old_price = old_price * float(current_price3)
    

        print(f'Name: {name}')
        print(f'Current Price: ${current_price2}')
        print(f'24H Change: {change}')
        print(f'Original Price: {"${:,.2f}".format(old_price)}')
        input()


#API
client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = '+16693568980'

myCellPhone = '+18477367388'


for row in rows[1:2]:
    td = row.findAll('td')
    if td:
        bit_price = td[3].text
        bit_price = bit_price.split('$')
        bit_price = bit_price[1]
        bit_price = bit_price.replace(',','')
        bit_price = float(bit_price)
       
if bit_price < 40000.00:
    textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,
                body=f'Bitcoin has fallen below $40,000\nPrice: {"${:,.2f}".format(bit_price)}')

for row in rows[2:3]:
    td = row.findAll('td')
    if td:
        eth_price = td[3].text
        eth_price = eth_price.split('$')
        eth_price = eth_price[1]
        eth_price = eth_price.replace(',','')
        eth_price = float(eth_price)

if eth_price < 3000.00:
    textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,
                body=f'Ethereum has fallen below $3,000\nPrice: {"${:,.2f}".format(eth_price)}')