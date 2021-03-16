import urllib.request, urllib.parse, urllib.error
import json

url = "http://py4e-data.dr-chuck.net/comments_1147561.json"
uh = urllib.request.urlopen(url) 
data = uh.read().decode()
print('Retrieved data:', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js:
    print('==============Failure To Retrieve ================')
    quit()

print(json.dumps(js, indent=4))
Sum = 0
for comment in js['comments']:
    Sum += int(comment['count'])

print(Sum)

