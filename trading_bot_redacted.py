import requests
import json
import hmac
import time
import hashlib
import base64
import datetime, time

#nonce, time, and keys in global variables to be used throughout
t = datetime.datetime.now()
payload_nonce = time.time()
gemini_api_key = ""
gemini_api_secret = "".encode()

#first call to get current market price
url = "https://api.gemini.com/v1/pubticker/btcusd"
payload =  {"request": "/v1/pubticker/btcusd", "nonce": payload_nonce}
encoded_payload = json.dumps(payload).encode()
b64 = base64.b64encode(encoded_payload)
signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

request_headers = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': "no-cache"
    }

response = requests.get(url, headers=request_headers)
prices = response.json()
current_price = (prices['ask'])
print(f"current bitcoin price is" + current_price)

time.sleep(0.05)

#second call to get last trade price and type
url2 = "https://api.gemini.com/v1/trades/btcusd"
payload2 = {"request": "/v1/trades/btcusd", "nonce": payload_nonce}
encoded_payload2 = json.dumps(payload2).encode()
b64_2 = base64.b64encode(encoded_payload2)
signature2 = hmac.new(gemini_api_secret, b64_2, hashlib.sha384).hexdigest()

request_headers2 = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64_2,
    'X-GEMINI-SIGNATURE': signature2,
    'Cache-Control': "no-cache"
}

response2= requests.get(url2, headers=request_headers2, limit_trades=1)
last_trade = response2.json()
last_trade_price = (last_trade['amount'])
print(f"last trade price was" + last_trade_price)

trade_type = response2.json()
last_trade_type = (trade_type['type'])
print(last_trade_type)

time.sleep(0.05)

#final call to get current account balance
url3 = "https://api.gemini.com/v1/positions"
payload3 = {"request": "/v1/positions", "nonce": payload_nonce}
encoded_payload3= json.dumps(payload3).encode()
b64_3 = base64.b64encode(encoded_payload3)
signature3 = hmac.new(gemini_api_secret, b64_3, hashlib.sha384).hexdigest()

request_headers3 = {
     'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64_3,
    'X-GEMINI-SIGNATURE': signature3,
    'Cache-Control': "no-cache"
}

response3 = requests.post(url3, headers=request_headers3)
acct = response3.json()
btc_balance = (acct['quantity'])
print(f"account balance is" + btc_balance + "bitcoin")
cash = (acct['availableForWithdrawal'])

time.sleep(0.05)

#initialize functions 

    ##define function for selling
def buy(current_price, last_trade_price):
    if ((current_price - last_trade_price) / last_trade_price) * 100 >= 5:
        url4 = "https://api.gemini.com/v1/order/new"
        payload4 = {"request": "/v1/order/new", "nonce": payload_nonce, "symbol": "btcusd", "amount": btc_balance, "price": current_price, "side": "sell", "type": "exchange limit", "options": ['maker-or-cancel']}
        encoded_payload4 = json.dumps(payload4).encode()
        b64_4 = base64.b64encode(encoded_payload4)
        signature4 = hmac.new(gemini_api_secret, b64_4, hashlib.sha384).hexdigest()

        request_headers4 = {
            'Content-Type': "text/plain",
            'Content-Length': "0",
            'X-GEMINI-APIKEY': gemini_api_key,
            'X-GEMINI-PAYLOAD': b64_4,
            'X-GEMINI-SIGNATURE': signature4,
            'Cache-Control': "no-cache"
        }
        response4 = requests.post(url4, data=None, headers = request_headers4)
        new_order = response.json()
        print(new_order)
    else:
        print("conditions not met.")

    ##3. define function for buying
def sell(current_price, last_trade_price):
    if ((last_trade_price - current_price) / last_trade_price) * 100 >= 5:
        url4 = url4
        payload5 = {"request": "/v1/order/new", "nonce": payload_nonce, "symbol": "btcusd", "amount": cash, "price": current_price, "side": "buy", "type": "exchange limit", "options": ['maker-or-cancel']} 
        encoded_payload5 = json.dumps(payload5).encode()
        b64_5 = base64.b64encode(encoded_payload5)
        signature4 = hmac.new(gemini_api_secret, b64_5, hashlib.sha384).hexdigest()

        request_headers5 = {
            'Content-Type': "text/plain",
            'Content-Length': "0",
            'X-GEMINI-APIKEY': gemini_api_key,
            'X-GEMINI-PAYLOAD': b64_5,
            'X-GEMINI-SIGNATURE': signature4,
            'Cache-Control': "no-cache"
        }
        response5 = requests.post(url4, data=None, headers = request_headers5)
        new_order = response.json()
        print(new_order)
    else:
        print("conditions not met.")

#choosing which function to use 
if last_trade_type == "buy":
    sell(current_price, last_trade_price)
elif last_trade_type == "sell":
    buy(current_price, last_trade_price)