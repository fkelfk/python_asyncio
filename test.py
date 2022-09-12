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


c = Counter()
i = iter(c)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for k in c:
#     print(k)


def test1():
    print("print 1")
    yield 1
    print("print 2")
    yield 2
    print("print 3")
    print("print 4")
    yield 3
    print("print 5")


def test2():
    for i in range(10):
        yield i * 2


g = test1()

print(type(g))
print(dir(g))
print(next(g))
print(next(g))
print(next(g))


for i in x:
    print i


def callee():
    yield 1
    yield 2
		
x = callee()
i = next(x)
i = next(x)