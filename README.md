# Head First - Programming with Python

## Cap. 2

```r
import urllib.request # library urllib.request
import time # library time
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
```

## Programming Toolbox

- Strings are sequences of individuals characters
- The characters of an string are identified by the index
- The values of the index are “deslocamentos” which start on ZERO
- The methods gives variables with built in functionalities
- The programming libraries provide an predefined  collection of codes and functions
- The variables has types (float, char,…)
- Number is type of data
- Strings are type of data

## Python Toolbox

- s[4]  access the 5th character of the variable “s” and it is an string
- s[b:12] access an substring inside the string “s” (until, but no inclusive)
- the method s.find( ) to search strings
- the method s.upper( ) for the conversion strings to UPPERCASE
- float( ) convert string to numbers with decimals
- the library urllib.request is used to communication with urls
- the library time is used to work with data