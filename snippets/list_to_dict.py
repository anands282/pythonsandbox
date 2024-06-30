#Merge two lists into a dictionary

key_lists = ['A', 'B', 'C']
value_lists = ['blue', 'red', 'bold']

dict_method1 = dict(zip(key_lists,value_lists))

print(dict_method1)

dict_method2 = {key: value for key, value in zip(key_lists, value_lists)}

print(dict_method2)

item_tuples = zip(key_lists, value_lists)
dict_method3= {}
for key, value in item_tuples:
    dict_method3[key] = value

print(dict_method3)