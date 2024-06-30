my_list = ["blue", "red", "green"]

#1- Using sort or srted directly or with specifc keys
my_list.sort() #sorts alphabetically or in an ascending order for numeric data
my_list = sorted(my_list, key=len) #sorts the list based on the length of the strings from shortest to longest.
# You can use reverse=True to flip the order

#2- Using locale and functools
import locale
from functools import cmp_to_key
my_list = sorted(my_list, key=cmp_to_key(locale.strcoll))