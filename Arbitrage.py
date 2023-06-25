#arbitrage
import json

curl https://api.coinbase.com/v2/prices/btc-usd/spot
#curl https://api.binance.com/api/v3/ticker/price/btcusdt '''need a vpn, this is binance international and can't find it for US'''

btc-usd/spot = {
    "data":
    {"base":"BTC",
     "currency":"USD",
     "amount":"30596.350000003575"}
     }

#grab price at binance

def find_arb():
    #if cb_price == b_price * .95:
        #buy on binance
    #if b_price == cb_price * .95:
        #buy on binance

#def sell function(sell_parameter) - sets up price to sell based on parameter. Maybe a 2% scalp

