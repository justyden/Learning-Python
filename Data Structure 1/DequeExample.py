class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueueStart(self, inputData):
        self.items.insert(0, inputData)

    def enqueueEnd(self, inputData):
        self.items.append(inputData)

    def dequeueStart(self):
        return self.items.pop(0)

    def dequeueEnd(self):
        return self.items.pop()


