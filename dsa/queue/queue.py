class Queue(object):
    def __init__(self, size):
        self.__maxSize = size
        self.__que = [None] * size
        self.__front = 1
        self.__rear = 0
        self.__num_items = 0

    def insert(self, item):
        if self.isFull():
            raise Exception("Queue overflow")
        self.__rear += 1
        if self.__rear == self.maxSize:
            self.__rear = 0
        self.__que[self.__rear] = item
        self.__num_items += 1
        return True

    def remove(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        front = self.__que[self.__front]
        self.__que[self.__front] = None
        self.__front += 1
        if self.__front == self.__maxSize:
            self.front = 0
        self.__num_items -= 1
        return front

    def peek(self):
        return None if self.isEmpty() else self.__que[self.__front]

    def isEmpty(self): return self.__num_items == 0

    def isFull(self): return self.__num_items == self.__maxSize

    def __len__(self): return self.__num_items

    def __str__(self):
        ans = "["
        for i in range(self.__num_items):
            if len(ans) > 1:
                ans += ", "
            j = i + self.__front
            if j >= self.__maxSize:
                j -= self.__maxSize
            ans += str(self.__que[j])
        ans += "]"
        return ans