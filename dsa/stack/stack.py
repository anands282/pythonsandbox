class Stack:
    def __init__(self, stack_height_max: int):
        self.__stack_list = [None] * stack_height_max
        self.__top = -1

    def push(self, item):
        self.__top += 1
        self.__stack_list[self.__top] = item

    def pop(self):
        top_item = self.__stack_list[self.__top]
        self.__stack_list[self.__top] = None
        self.__top -= 1
        return top_item

    def peek(self):
        if not self.is_empty():
            return self.__stack_list[self.__top]

    def is_empty(self):
        return self.__top == -1

    def is_full(self):
        return self.__top >= len(self.__stack_list) - 1

    def __len__(self):
        return self.__top + 1

    def __str__(self):
        ans = "["
        for i in range(self.__top + 1):
            if len(ans) > 1:
                ans += ", "
        ans += str(self.__stack_list[i])
        ans += "]"
        return ans


