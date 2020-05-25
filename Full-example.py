import urllib.request, json

# Opening a web request
url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=n&apiKey=e2af8afad2510d9e0fee")
# Decoding response to str
data = json.loads(url.read().decode()) # Decoding a web request

# Parsing results
results = data['results']
USD_ILS = results['USD_ILS']
val = USD_ILS['val']
print(val)
