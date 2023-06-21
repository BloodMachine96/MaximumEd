word_input = input()
lenght = len(word_input) // 2
print(word_input[:lenght] == word_input[:len(word_input)-lenght-1:-1])