# create stocks with their price
stocks = {"AAPL": 187.31, "MSFT": 124.06, "FB": 183.50, "SOL": 99}

# set my own limits to buy
buy_limits = {"MSFT": 120, "SOL": 100.0}

# loop through every stock and price
for key, value in stocks.items():
    # print the stock and price
    print(f"{key}: {value}")
    # get the price if it exists in my limits
    limit_price = buy_limits.get(key)

    # if the price exists in my limits
    if limit_price is not None:
        # if the price is less than my limit
        if value < limit_price:
            # buy that!
            print(f"buy {key} now!!")