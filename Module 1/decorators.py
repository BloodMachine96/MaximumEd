import time


def hello(a):
    start = time.time()
    result = []
    for i in range(a):
        result.append(i)
    
    print(sum(result))
    print(time.time() - start)


def hello_2():
    print('1')


hello(10000000)