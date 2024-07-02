import pyotp
import robin_stocks.robinhood as robin

class RobinhoodStockTrader:
    def __init__(self, api_key, private_key_base64, public_key_base64):
        self.api_key = api_key
        self.private_key_base64 = private_key_base64
        self.public_key_base64 = public_key_base64
        self.login()

    def login(self):
        KEY = 'your_key'
        EMAIL = 'your_email'
        PASSWD = 'your_password'
        totp = pyotp.TOTP(KEY).now()
        robin.login(EMAIL, PASSWD, mfa_code=totp)

    def buy_stock(self, symbol, quantity):
        try:
            result = robin.orders.order_buy_market(symbol, quantity)
            return f"Bought {quantity} of {symbol}. Transaction: {result}"
        except Exception as e:
            return f"Error buying stock: {str(e)}"

    def sell_stock(self, symbol, quantity):
        try:
            result = robin.orders.order_sell_market(symbol, quantity)
            return f"Sold {quantity} of {symbol}. Transaction: {result}"
        except Exception as e:
            return f"Error selling stock: {str(e)}"

    def get_quote(self, symbol):
        try:
            price = robin.stocks.get_latest_price(symbol)[0]
            return f"{symbol.upper()}: ${price}"
        except Exception as e:
            return f"Error fetching quote: {str(e)}"
