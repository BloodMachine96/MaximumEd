# Асимптотическая сложность - способ подсчёта необходимых 
# O(N) - описать наихудший из сценариев работы программы
# O(N**2)
# O(Log(N)) - лучший? Сказали с двойным основанием 

# def strcount(s): #ПЛОХАЯ СЛОЖНОСТЬ O(N*M)
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)

# strcount('abac')

def strcount(s): # O(N)
    dct = {}
    for sym in s:
        dct[sym] = dct.get(sym, 0) + 1
    
    for key, value in dct.items():
        print(key, value)

strcount('abac')