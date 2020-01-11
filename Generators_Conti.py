def special_func(it):
    iterator = iter(it)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_func([1,2,2,4])

class rangefunction():
    current = 0
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if rangefunction.current < self.stop:
            num = rangefunction.current
            rangefunction.current += 1
            return num
        raise StopIteration

ran = rangefunction(0,100)
for i in ran:
    print(i)
