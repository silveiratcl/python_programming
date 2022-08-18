import urllib.request

page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
text = page.read().decode("utf8")

print(text)

# the challenge is to scrap only the price $6.85
# Here my code modification to get only the price by counting the elementes
# of the text

import urllib.request

page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
text = page.read().decode("utf8")
price = text[234:238]

print(price)


# challenge 2
# The price position varies along the html code
# the challenge is to "find" some charaters to track the price

import urllib.request

page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
text = page.read().decode("utf8")
where = text.find(">$")

start_price = where + 2
end_price = start_price + 4

price = text[start_price:end_price]

print(price)


# challenge #4
# The price position varies along the html code
# the challenge is to "find" some charaters to track the price
# print if the price while $ > 4.74

import urllib.request # library
price = 99.99
while price > 4.74:

    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html") # library.function()
    text = page.read().decode("utf8")
    where = text.find(">$")

    start_price = where + 2
    end_price = start_price + 4

    price = float(text[start_price:end_price])

print("Buy!")





# challenge #5
# limit the number of requests by time using the library "time"

import urllib.request # librar yurllib.request
import time
price = 99.99
while price > 4.74:

    time.sleep(900)
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html") # library.function()
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_price = where + 2
    end_price = start_price + 4
    price = float(text[start_price:end_price])

print("Buy!", time_read)