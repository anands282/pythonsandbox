#Formatting strings with f string.
str_val = 'books'
num_val = 15
print(f'{num_val} {str_val}') # 15 books
print(f'{num_val % 2 = }') # 1
print(f'{str_val!r}') # books

#Dealing with floats
price_val = 5.18362
print(f'{price_val:.2f}') # 5.18

#Formatting dates
from datetime import datetime;
date_val = datetime.utcnow()
print(f'{date_val=:%Y-%m-%d}') # date_val=2021-09-24