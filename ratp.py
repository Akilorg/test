import requests
import time

url = "https://api-ratp.pierre-grimaud.fr/v4/traffic/metros/7"
response = requests.get(url)
i = 1
while i ==1 :
    if response.status_code == 200:
        data = response.json()
        message = data['result']['title']
        print(message)
        time.sleep(400)
    else:
        print("Une erreur s'est produite. Le code d'erreur est : ", response.status_code)
