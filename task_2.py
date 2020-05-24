stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_price = 0

for key, value in stock.items():
    total_price += float(stock[key]) * float(prices[key])

print(total_price)