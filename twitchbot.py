import websocket
import ssl
import sys
import threading

class TwitchBot:
    def __init__(self, oauth_token, nick, channel, stock_trader):
        self.oauth_token = oauth_token
        self.nick = nick
        self.channel = channel
        self.ws = None
        self.stock_trader = stock_trader

    def extract_username(self, message):
        parts = message.split(":", 2)
        if len(parts) >= 2:
            user_info = parts[1].split("!", 1)
            if len(user_info) >=2:
                return user_info[0]
        return ""

    def on_message(self, ws, message):
        if "PRIVMSG" in message:
            parts = message.split(":", 2)
            if len(parts) >= 3:
                username = self.extract_username(message)
                # channel_message = f"#{username} :{parts[2].strip()}"
                # print(f"Message Received: {channel_message}\n")
                if "!buy" in parts[2].strip().lower():
                    self.handle_buy_command(ws, username, parts[2].strip())
                    #symbol = parts[2].strip().split()[1]
                    #self.send_message(ws, f"@{username} Bought {symbol}")
                    #print(f"BUY {symbol} {username}")
                elif "!sell" in parts[2].strip().lower():
                    self.handle_sell_command(ws, username, parts[2].strip())
                    #symbol = parts[2].strip().split()[1]
                    #self.send_message(ws, f"@{username} Sold {symbol}")
                    #print(f"SELL {symbol} {username}")
                elif "!hi" in parts[2].strip().lower():
                    self.send_message(ws, f"@{username} Hi there!")
        else:
            print(f"Message Received: {message}")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def on_open(self, ws):
        ws.send(f"PASS {self.oauth_token}")
        ws.send(f"NICK ListenerBot")
        ws.send(f"JOIN #{self.channel}\n")

    def send_message(self, ws, message):
        ws.send(f"PRIVMSG #{self.channel} :{message}")

    def listen_input(self, ws):
        while True:
            user_input = input()
            if user_input.lower() in {"quit", "exit", "close"}:
                ws.close()
                sys.exit(0)

    def handle_buy_command(self, ws, username, command):
        parts = command.split()
        if len(parts) == 2:
            symbol = parts[1]
            quantity = 1
            response = self.stock_trader.buy_stock(symbol, quantity)
            self.send_message(ws, f"@{username} {response}")
        else:
            self.send_message(ws, f"@{username} Invalid commmand format. Use: !buy <symbol>")

    def handle_sell_command(self, ws, username, command):
        parts = command.split()
        if len(parts) == 2:
            symbol = parts[1]
            quantity = 1
            response = self.stock_trader.sell_stock(symbol, quantity)
            self.send_message(ws, f"@{username} {response}")
        else:
            self.send_message(ws, f"@{username} Invalid commmand format. Use: !sell <symbol>")

    def run_bot(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("wss://irc-ws.chat.twitch.tv:443/", 
                                    on_message=self.on_message, 
                                    on_error=self.on_error, 
                                    on_close=self.on_close)
        self.ws.on_open = self.on_open
        
        threading.Thread(target=self.listen_input, args=(self.ws,), daemon=True).start()
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        print("\nClosing bot...")




