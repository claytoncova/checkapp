''' check web app avaliability '''
import requests
import sys
import getopt

def get_help(error):
    """Standard output and Usage instructions"""
    print('Usage:')
    print('checkapp.py <url>')
    if error:
        sys.exit(2)
    else:
        sys.exit()

def get_response(url):
  try:
    response = requests.get(url[0], timeout = 5)
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

def main(argv):
  #Tratamento de parâmetros na linha de comando
  if len(sys.argv) == 1:
      get_help(False)
  else:
      try:
          opts = getopt.getopt(argv, "h")
      except getopt.GetoptError:
          get_help(True)
  for opt in opts:
      if opt == '-h':
          get_help(False)
  get_response(argv)

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass

    finally:
        sys.exit
