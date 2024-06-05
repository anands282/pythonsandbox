from stack import Stack


word = input("Eneter the word to revers: ")
length = len(word)
stack = Stack(length)

for letter in word:
    stack.push(letter)

reverse = ''
while not stack.is_empty():
    reverse += stack.pop()

print("revers word : "+ reverse)