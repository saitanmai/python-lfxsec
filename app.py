
import requests
import flask
import django


resp = requests.get("https://ipinfo.io")

print(resp.json())
