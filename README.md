# Twitch Chat Bot

## Overview
This project contains a Twitch chat bot that allows users to interactively trade stocks using commands in the chat. The bot listens for specific commands related to buying and selling stocks, communicates with the Robinhood API for executing trades, and provides feedback to users in the chat.

## Features
- Listens to Twitch chat for commands related to stock trading.
- Supports commands for buying and selling stocks.
- Utilizes IRC, WebSockets, and SSL verification for secure communication with Twitch.
- Uses threading for concurrent processing of chat messages and trading operations.
- Integrates with the Robinhood API for executing trades.
- Provides feedback and confirmation messages in the chat.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/twitch-stock-trading-bot.git
    cd twitch-stock-trading-bot
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    pip install robin-stocks
    ```

3. Obtain the necessary API keys:
    - Twitch OAuth token: Generate from [Twitch Apps TMI](https://twitchapps.com/tmi/).
    - Robinhood API key: Obtain from [Robinhood API Credentials Portal]().

## Configuration
1. Open main.py and enter your Twitch OAuth token, Twitch channel, and Robinhood API keys.

## Usage
1. Start the Twitch bot:
    ```bash
    python main.py
    ```

2. Join your Twitch channel and interact with the bot using commands like !buy <symbol> and !sell <symbol> .

## Commands
- !buy &lt;symbol&gt;: Buy the specified stocks for the given symbol.
- !sell &lt;symbol&gt;: Sell the specified stocks for the given symbol.
- !view &lt;symbol&gt;: View the current price of the specified stock symbol.

## Directory Structure
- main.py: Entry point for running the Twitch bot and stock trading functionalities.
- requirements.txt: Contains the required Python packages for the project.
- stocktrader.py: Handles the interactions with the Robinhood API for buying and selling stocks.
- twitchbot.py: Implements the Twitch chat bot functionalities using IRC, WebSockets, and SSL.
- twitchoauth.py: Helps with getting an oAuth token for Twitch, or you can use [TwitchApps](https://twitchapps.com/tmi/) to get your token.

## Documentation
For more details on the Robinhood API for crypto trading, refer to the [Robinhood API Documentation](https://docs.robinhood.com/crypto/trading/).
