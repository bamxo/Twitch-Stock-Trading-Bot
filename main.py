from twitchbot import TwitchBot
from stocktrader import RobinhoodStockTrader

# Twitch Bot Credentials
oauth_token = "oauth_token" # Replace 'oauth_token' with your generate oAuth Token
nick = "ListenerBot"
channel = "your_channel_name" # Replace 'your_channel_name' with your channel

# Robinhood API Credentials
api_key = 'api_key' # Replace 'api_key' with your API Key
private_key_base64 = 'private_key' # Replace 'private_key' with your Private Key
public_key_base64 = 'public_key' # Replace 'public_key' with your Public Key

def main():
    stock_trader = RobinhoodStockTrader(api_key, private_key_base64, public_key_base64)
    
    twitch_bot = TwitchBot(oauth_token, nick, channel, stock_trader)
    twitch_bot.run_bot()

if __name__ == "__main__":
    main()



