#!/usr/bin/python3
import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    content_type = type(response.text)
    content = response.text.strip()
    
    print("Body response:")
    print("\t- type: {}".format(content_type))
    print("\t- content: {}".format(content))
