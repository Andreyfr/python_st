import requests

payload = {
    'inUserName': 'USERNAME',
    'inUserPass': 'PASSWD'
}
url_login = "https://itunesconnect.apple.com/login"
url_auth =  "https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1056662247/ios/"

with requests.Session() as s:
    p = s.post(url_login, data=payload)
    print (p.status_code)
    print (p.text)
    r = requests.get(url_auth)
    print (r.status_code)
    print (r.headers)
