import requests
from bs4 import BeautifulSoup
import smtplib
import time

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

def sendEmail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('Charpee6464@gmail.com', 'etojoedpxlknqbzh')

    subject = 'The price fell down on the item you want to buy'
    body = "Check the link:",URL,"."

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'Charpee6464@gmail.com',
        'Lobstergoat64@gmail.com',
        msg
    )

    print("Email sent")
    server.quit()


def checkPriceA():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    #print(soup.prettify)

    title = soup.find(id="productTitle").getText()
    price = soup.find(id="priceblock_ourprice").getText()

    convertedP = int(price[1:4])

    print(title.strip())
    print("The price of the item is",convertedP,"Pounds")

    if convertedP < maxPrice:
        sendEmail()
    else:
        print("")
        print("Price of item is higher than max")

def checkPriceE():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    #print(soup.prettify)

    price = soup.find(id="prcIsum").getText()
    convertedP = int(price[1:4])
    print("The price of the item is",convertedP,"Pounds")

    if convertedP < maxPrice:
        sendEmail()
    else:
        print("")
        print("Price of item is higher than max")


site = input("Which site are you using? (Amazon)(Ebay)")
if site == "Amazon":
    print("")
    URL = input("Please enter a the URL of the item you wish to buy: ")
    maxPrice = int(input("Please enter the max amount of money you would pay for this item: £"))
    print("")
    checkPriceA()
if site == "Ebay":
    URL = input("Please enter a the URL of the item you wish to buy: ")
    maxPrice = int(input("Please enter the max amount of money you would pay for this item: £"))
    checkPriceE()


#while(True):
    #checkPriceA()
    #print("Price Checked")
    #time.sleep(86400)
