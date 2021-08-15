# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    stock_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            num_share = int(row[1])
            stock_price = float(row[2])
            stock_cost += num_share * stock_price
    return stock_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)