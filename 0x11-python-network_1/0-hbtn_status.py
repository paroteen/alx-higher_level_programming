#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')

        print("Body response:")
        print("    - type:", type(body))
        print("    - content:", body)
        print("    - utf8 content:", utf8_content)
except urllib.error.URLError as e:
    print("Error:", e)

