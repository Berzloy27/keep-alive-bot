import requests
import os

def keep_alive():
  url = f"https://{os.environ[imshop]}.repl.co/"
  try:
    response = requests.get(url)
    print(f"Keep-alive request sent to {url}")
  except Exception as e:
    print(f"Error sending keep-alive request: {e}")

if __name__ == "__main__":
  keep_alive()
