import requests
import base64
import hashlib
import hmac
import json
import time

class RobinhoodStockTrader:
    def __init__(self, api_key, private_key_base64, public_key_base64):
        self.api_key = api_key
        self.private_key_base64 = private_key_base64
        self.public_key_base64 = public_key_base64
        self.base_url = "https://api.robinhood.com"

    def generate_signature(self, message):
        private_key_bytes = base64.b64decode(self.private_key_base64)
        public_key_bytes = base64.b64decode(self.public_key_base64)

        private_key = hmac.new(private_key_bytes, message.encode(), hashlib.sha256).digest()
        signature = base64.b64decode(private_key).decode("utf-8")
        return signature
    
    def generate_headers(self, path, method, body=""):
        timestamp = str(int(time.time()))
        message = f"{self.api_key}{timestamp}{path}{method}{body}"
        signature = self.generate_signature(message)

        headers = {
            "x-api-key": self.api_key,
            "x-signature": signature,
            "x-timestamp": timestamp
        }
        return headers
    
    def buy_stock(self, symbol, quantity):
        endpoint = "/api/v1/crypto/trading/orders"
        url = f"{self.base_url}{endpoint}"

        body = {
            "client_order_id": str(int(time.time())),
            "side": "buy",
            "symbol": symbol,
            "type": "market",
            "market_order_config": {
                "asset_quantity": quantity
            }
        }

        headers = self.generate_headers(endpoint, "POST", json.dumps(body))
        response = requests.post(url, headers=headers, json=body)

        if response.status_code == 200:
            return "Successfully bought stocks."
        elif response.status_code == 400:
            return "Bad request. Check your input data."
        elif response.status_code == 401:
            return "Unauthorized. Check your API credentials."
        elif response.status_code == 403:
            return "Forbidden. Access denied."
        elif response.status_code == 404:
            return "Not found. Endpoint not found."
        elif response.status_code == 405:
            return "Method not allowed. Check your request method."
        elif response.status_code == 406:
            return "Not acceptable. Check your request headers."
        elif response.status_code == 415:
            return "Unsupported media type. Check your request content type."
        elif response.status_code == 429:
            return "Too many requests. Rate limit exceeded."
        elif response.status_code == 500:
            return "Internal server error. Try again later."
        elif response.status_code == 503:
            return "Service unavailable. Try again later."
        else:
            return "Unknown error occurred."
        
    def sell_stock(self, symbol, quantity):
        endpoint = "/api/v1/crypto/trading/orders"
        url = f"{self.base_url}{endpoint}"

        body = {
            "client_order_id": str(int(time.time())),
            "side": "sell",
            "symbol": symbol,
            "type": "market",
            "market_order_config": {
                "asset_quantity": quantity
            }
        }

        headers = self.generate_headers(endpoint, "POST", json.dumps(body))
        response = requests.post(url, headers=headers, json=body)

        if response.status_code == 200:
            return "Successfully sold stocks."
        elif response.status_code == 400:
            return "Bad request. Check your input data."
        elif response.status_code == 401:
            return "Unauthorized. Check your API credentials."
        elif response.status_code == 403:
            return "Forbidden. Access denied."
        elif response.status_code == 404:
            return "Not found. Endpoint not found."
        elif response.status_code == 405:
            return "Method not allowed. Check your request method."
        elif response.status_code == 406:
            return "Not acceptable. Check your request headers."
        elif response.status_code == 415:
            return "Unsupported media type. Check your request content type."
        elif response.status_code == 429:
            return "Too many requests. Rate limit exceeded."
        elif response.status_code == 500:
            return "Internal server error. Try again later."
        elif response.status_code == 503:
            return "Service unavailable. Try again later."
        else:
            return "Unknown error occurred."
        

