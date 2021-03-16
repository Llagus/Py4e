from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags

tags = soup("a")
count = 7
lst = list()

while count > 0:
    lst.append(tags[17].contents[0])
    html = urlopen(tags[17].get('href'), context = ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    count -= 1

print(lst)
    