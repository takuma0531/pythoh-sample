import requests;
import time;

response = requests.get('https://api.covid19api.com/country/south-africa/status/confirmed')
print(response)

print('status_code', response.status_code)
print(response.json())
print(response.text)
time.sleep(10)