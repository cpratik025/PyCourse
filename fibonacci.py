def fib(number):
    a = 0
    b = 1
    res = []
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

    for i in range(number):
        res.append(a)
        temp = a
        a = b
        b = temp + b
    print(res)
for x in fib(20):
    print(x)

my_var = 7
print(type(my_var))
