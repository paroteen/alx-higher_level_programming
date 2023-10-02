#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        utf8_content = body.decode("utf-8")

        print("Body response:$")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(repr(body)))
        print("\t- utf8 content: {}".format(utf8_content))
