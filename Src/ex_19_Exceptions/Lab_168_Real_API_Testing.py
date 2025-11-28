from logging import exception

import requests
try:
 url= input("Enter the URL")
#response= requests.get("https://google.com")
 response= requests.get(url)

 print(response.status_code)
except requests.exceptions.ConnectionError:
    print("Error due to the wrong URL or Connection failed")
except requests.exceptions.Timeout:
    print("Time out error, not able to load the URL")
except Exception as e:
    print("e")