# find the n largest or smallest N items in collection
# the heapq module has two functions nlargest() and nsmallest() that do exactly this
import heapq

nums = [1, 3, 5, 2, 6, 7, 4, 2, 10, 11, 34]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
             {'name': 'AAPL', 'shares': 50, 'price': 543.22},
             {'name': 'FB', 'shares': 200, 'price': 21.09},
             {'name': 'HPQ', 'shares': 35, 'price': 31.75}
]
print(heapq.nlargest(3, portfolio, key=lambda p: p['price']))
