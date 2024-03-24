import urllib.request
url = 'https://alu-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))
except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code)
