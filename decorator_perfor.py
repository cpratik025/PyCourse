from time import time

def performance(funct):
    def wraper_function(*args,**kwargs):
        time1 = time()
        result = funct(*args,**kwargs)
        time2= time()
        print(f'It took {time2-time1} millisecond')
        return result
    return wraper_function
@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()