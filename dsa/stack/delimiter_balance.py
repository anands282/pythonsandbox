from stack import Stack

stack = Stack(100)

expr = input("enter the expression: ")
errors = 0

for pos,letter in enumerate(expr):
    if letter in "{[(":
        if stack.is_full():
            raise Exception('Stack overflow on expression')
        else:
            stack.push(letter)

    elif letter in "}])":
        if stack.is_empty():
            print("Error")
            errors += 1
        else:
            left = stack.pop()
            if not (left == "{" and letter == "}" or
                    left == "[" and letter == "]" or
                    left == "(" and letter == ")"):
                print("Error")
                errors += 1

if stack.is_empty() and errors == 0:
    print("balanced expression")
else:
    print("unbalanced")
