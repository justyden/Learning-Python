class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, inputData):
        self.items.append(inputData)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return 0
        elif len(self.items) == 1:
            return self.items[0]
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)
