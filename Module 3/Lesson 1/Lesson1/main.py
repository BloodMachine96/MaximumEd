# Чтоб добавить в словарь my_dict['номер'] = 'Никита', т.е. новый ключ в кв. скобочках и затем новое значение
# Чтобы удалить либо remove, либо pop
# Асимптотика
# -1 в списке = последний элемент
# Цикл for:
# for i in range(5,10):
#   print(i)
# (start, stop, step)
# Итерация = вывести один раз имя тела
# Конструктор классов def __init__(self, ...(параметры))
 








# class Employee():
#     def __init__(self, name, sal):
#         self.name = name
#         self.sal = sal

# first_employee = Employee('Никита', 1000)

# print(f'У {first_employee.name} {first_employee.sal} рублей')

# employee = {
#     'name': 'Вадим',
#     'salary': 199,
#     'age': 16,
# }

# print(f"{employee['name']} зарплата составляет {employee['salary']}")

# employees_list = [
#     {
#         'name': 'Вадим',
#         'salary': 199,
#     },

#     {
#         'name': 'Сева',
#         'salary': 200_000
#     },

#     {
#         'name': 'Никита',
#         'salary': 0

#     }
# ]

# for employee in employees_list:
#     print(f"Имя: {employee['name']}, Зарплата: {employee['salary']}")





class Employee:
    def __init__(self, salary, name, on_vacation, is_good_employee):
        self.is_good_employee = is_good_employee
        self.salary = salary
        self.name = name
        self.on_vacation = on_vacation

first_employee = Employee(1000, 'Никита', True, True)
second_employee = Employee(900, 'Генадий', False, True)
third_employee = Employee(1100, 'Максим', False, True)
fourth_employee = Employee(50, 'Ошибки', False, False)
fifth_employee = Employee(1500, 'Астат', False, True)

employee_list = [
    {'Имя' : first_employee.name,
     'Зарплата' : first_employee.salary,
     'На отдыхе' : first_employee.on_vacation,
     'Хороший работник' : first_employee.is_good_employee
     },
     {'Имя' : second_employee.name,
     'Зарплата' : second_employee.salary,
     'На отдыхе' : second_employee.on_vacation,
     'Хороший работник' : second_employee.is_good_employee
     },
     {'Имя' : third_employee.name,
     'Зарплата' : third_employee.salary,
     'На отдыхе' : third_employee.on_vacation,
     'Хороший работник' : third_employee.is_good_employee
     },
     {'Имя' : fourth_employee.name,
     'Зарплата' : fourth_employee.salary,
     'На отдыхе' : fourth_employee.on_vacation,
     'Хороший работник' : fourth_employee.is_good_employee
     },
     {'Имя' : fifth_employee.name,
     'Зарплата' : fifth_employee.salary,
     'На отдыхе' : fifth_employee.on_vacation,
     'Хороший работник' : fifth_employee.is_good_employee
     },
]

print(employee_list)

for i in employee_list:
    if i['Хороший работник'] == False:
        employee_list.remove(i)
    

print(employee_list)