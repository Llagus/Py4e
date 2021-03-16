import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

Sum = 0
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)

    comments = tree.findall('comments/comment')
    for comment in comments:
        Sum += int (comment.find('count').text)
    break

print('Count:',len(comments)) 
print('Sum:', Sum)
