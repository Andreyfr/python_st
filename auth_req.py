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

    
#Using disable_warnings (InsecureRequestWarning) will disable any output from the script when trying to log in to sites 
#with unverified SSL certificates.
import requests
from requests.packages.urllib3.exceptions 
import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
payload = {
    'inUserName': 'USERNAME',
    'inUserPass': 'PASSWD'
}
url = 'https://itunesconnect.apple.com/login'
r = requests.post(url, data=payload, verify=False)

print(r.status_code)
