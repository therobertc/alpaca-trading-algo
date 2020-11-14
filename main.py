#import alpaca_trade_api
import alpaca_trade_api as tradeapi
import time


#live_trading_key
#paper trading key
key = "INSERT API KEY ID"
sec = "GENERATE NEW API SECRET KEY"

#API endpoint URL
url = "https://paper-api.alpaca.markets"

#api_versions
#important to read documentation on version updates
api = tradeapi.REST(key, sec, url, api_version='v2')

account = api.get_account()

#Should print 'ACTIVE'
print(account.status)

#Place buy order:
#When placing orders, use the API
#api.submit_order() allows you to pass params to place order
#Example buy order:
#time_in_force="gtc"


#All args in the submit_order() MUST BE STR!
#Symbol means the stock ticker (FB, APPL, IBM,)
#qty means quantity
#side means buy or sell
#type means market or limit
#if using limit orders add
#limit_price=20.50

order = api.submit_order(symbol="NIO",
                        qty="100",
                        side="buy",
                        type="market",
                        time_in_force="day")

time.sleep(5)

print(order)
