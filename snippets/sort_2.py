a = ['blue', 'green', 'orange', 'purple', 'yellow']
b = [3, 2, 5, 4, 1]
#Use list comprehensions to sort these lists
sortedList =  [val for (_, val) in sorted(zip(b, a), key=lambda x: \
          x[0])]