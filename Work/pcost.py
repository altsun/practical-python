# pcost.py
#
# Exercise 1.27
stock_cost = 0.0
with open('Data/portfolio.csv', 'r') as f:
    headers = next(f)
    for line in f:
        stock_data = line.strip().split(',')
        num_share = int(stock_data[1])
        stock_price = float(stock_data[2])
        stock_cost += num_share * stock_price
print('Total cost:', stock_cost)