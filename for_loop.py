klines = [
    [
        57823875, # open price
        3578295, # close price
        235235,
        235235,
        235235,
        23523523
    ],
    [
        329308, # open price
        6489309, # close price
        'hello'
    ]
]
my_dictionary = { 'symbol': 'USDT', 'interval': '1m' }

new_data = []

for kline in klines:
    candlestick = {
        "open_price": kline[0],
        "close_price": kline[1]
    }
    new_data.append(candlestick)

print(new_data)
