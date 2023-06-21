def palindromcheck(string):
    reversed_str = string[::-1]
    return string == reversed_str
print(palindromcheck('лепсспел'))
print(palindromcheck('helloworld'))