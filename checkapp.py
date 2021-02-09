''' check web app avaliability '''
import requests

try:
  response = requests.get('http://fsdfsdfsdfs.net/', timeout = 5)
except requests.exceptions.SSLError as err:
  print("SSL error: {0}".format(err))
  response = None
except requests.exceptions.Timeout as err:
  print("Timeout...")
  response = None
except requests.exceptions.ConnectionError as err:
  print("Host unreacheable...")
  response = None

if (response != None and response.status_code == 200):
  print('App online.')
else:
  print('App Offline.')



