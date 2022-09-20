class Counter(object):
    def __iter__(self):
        iter = Iterator()
        return iter


class Iterator(object):
    def __init__(self):
        self.index = 0

    def __next__(self):
        if self.index > 10:
            raise StopIteration
        n = self.index * 2
        self.index += 1
        return n
