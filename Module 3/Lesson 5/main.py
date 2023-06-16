# import time

# class CodeTimer:
#     def __init__(self):
#         self.start = None

#     def __enter__(self):
#         self.start = time.time()
    
#     def __exit__(self, exc_val, exc_type, exc_tb):
#         # print(exc_type, exc_tb, exc_val)

#         t = time.time() - self.start
#         print("Итого время работы кода составило ", t, "сек.")

#         return True

# timer = CodeTimer()

# with timer:
#     l = [i for i in range(100)]
#     l[101]

# -------------------------------------------------
import random 

# my_list = [1,2,3]

# for i in my_list:
#     print(i)

# iterator = iter(my_list)

# for i in iterator:
#     print(i)

# for i in iterator:
#     print(i)

# # print(next(iterator))

# class RandomIter:
#     def __init__(self, limit):
#         self.limit = limit

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.limit == 0:
#             raise StopIteration
#         self.limit -= 1

#         return random.randint(0,100)
    
# for i in RandomIter(10):
#     print(i)
    
# random_iterator = RandomIter(10)

# for i in random_iterator:
#     print(i)

# ----------------------

# import sys


# class ThreadRedirect:
#     def __init__(self):
#         self.stdout = sys.stdout

#     def __enter__(self):
#         sys.stdout == sys.stderr

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         sys.stdout = self.stdout

# with ThreadRedirect():
#     print("Hello, world!")

class MyFile: 
    def __init__(self, filename, mode, encoding='utf-8'): 
        self.filename = filename 
        self.mode = mode 
        self.encoding = encoding 
 
    def __enter__(self): 
        self.file = open(self.filename, self.mode, encoding=self.encoding) 
        return self.file 
 
    def __exit__(self, exc_type, exc_val, exc_tb): 
        self.file.close()


with MyFile('file.txt', 'r', encoding='utf-8') as file:
    contaiment_text = file.read() 
    print(contaiment_text) 

# class InfiniteIteration:
#     def __init__(self, start):
#         self.start = start

#     def __iter__(self): 
#         return self 
 
#     def __next__(self): 
#         self.start += 1 
#         return self.start
    

# for i in InfiniteIteration(0): 
#     print(i)