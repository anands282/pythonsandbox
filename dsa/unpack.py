# you need to unpack N elements from an iterable, but the iterable maybe longer than N elements
grades = [99.9, 97, 96, 95, 94, 93.2]
first, *middle, last = grades
print(first)
print(middle)
print(last)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
firstone, *lastone = line.split(':')
print(firstone)
print(lastone)
