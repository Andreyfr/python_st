import requests

url = 'https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1056662247/ios/'
r = requests.get(url)

print (r.status_code)
print (r.headers)
