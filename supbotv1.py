import urllib.request, json

url = urllib.request.urlopen("https://www.supremenewyork.com/mobile_stock.json")
data = json.loads(url.read().decode())

json.parse(data)
