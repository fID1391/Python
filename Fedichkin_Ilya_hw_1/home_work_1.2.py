# Федичкин Илья Дмитриевич
# Факультет Python-разработки
# Основы языка Python
# Lesson 1 task 2

def funct(arg):
    global_summ = 0
    for i in range(len(arg)):
        some_variable = arg[i]
        summ_of_numbers = 0
        while some_variable > 0:
            summ_of_numbers = summ_of_numbers + some_variable % 10
            some_variable = some_variable // 10
        if summ_of_numbers % 7 == 0:
            global_summ = global_summ + arg[i]
    return (global_summ)

cube_list = list(i**3 for i in range(1, 1001, 2))
print(funct(cube_list))

for i in range(len(cube_list)):
    cube_list[i] += 17
print(funct(cube_list))