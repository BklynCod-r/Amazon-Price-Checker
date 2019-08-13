import requests
from bs4 import BeautifulSoup
import smtplib
import time

# You can put in any amazon link you want here within the ' '
URL = ''

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

def check_price():
    page = requests.get(URL, headers= headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    soup1 = BeautifulSoup(soup.prettify(), "html.parser")

    # This scrapes the product title 
    title = soup1.find(id="productTitle").get_text()

    # this scrapes the price as a String
    price = soup1.find(id="priceblock_ourprice").get_text()

    # convert price from String to float
    converted_price = float(price[1:5])

    # This checks to see if the item is under a 
    # certain amount you are willing to buy it for
    if(converted_price < 1000.0):
        send_mail()

    print(converted_price)
    print(title.strip())

# function will work only for gmail 
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Pass email and password or Two Factor Authorization(2FA) password
    # For parameters for server.login
    # i.e) server.login('john.doe@mail.com','password123')
    server.login('', '')
    subject = 'Price fell down!'
    body = 'Check the amazon link' + URL

    # This is a message formatter
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        # Two parameters are passed here
        # sender and receiver
        '', # Sender, i.e) john.doe@mail.com
        '', # Receiver i.e) mary.doe@mail.com
         msg
    )

    #This notifies us if email has been sent
    print('Hey email has been sent!')
    server.quit()

while(True):
    check_price()
    time.sleep(60) # 60 = 1 min, 60 * 60 = 1 hour, will notifiy us about prices on these occurences
