import requests, json

base_url = "https://api.sandbox.gemini.com/v1"
response1 = requests.get(base_url + "/pubticker/btcusd")
btc_data = response1.json()

response2 = requests.get(base_url + "/pubticker/ethbtc")
eth_data = response2.json()

print(btc_data)
print(btc_data['bid'])

print(eth_data)