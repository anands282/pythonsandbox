str1 = "hello"
str2 = "?"

def str_size(s):
  return len(s.encode('utf-8'))

str_size(str1)
str_size(str2)