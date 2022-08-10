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