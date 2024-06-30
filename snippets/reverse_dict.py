my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#Invert the dictionary based on its content
#1- If we know all values are unique.
my_inverted_dict = dict(map(reversed, my_dict.items()))

#2- If non-unique values exist
from collections import defaultdict
my_inverted_dict = defaultdict(list)
{my_inverted_dict[v].append(k) for k, v in my_dict.items()}

#3- If any of the values are not hashable
my_dict = {value: key for key in my_inverted_dict for value in my_inverted_dict[key]}