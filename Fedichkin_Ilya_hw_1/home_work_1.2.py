# Федичкин Илья Дмитриевич
# Факультет Python-разработки
# Основы языка Python
# Lesson 1 task 2

cube_list = []
summ_var_a = 0
summ_var_b = 0

# Вариант а)
for cube in range(1, 1001, 2):
    cube_list.append(cube**3)
for i in range(len(cube_list)):
    number = cube_list[i]
    summ = 0
    while number > 0:
        num = number % 10
        number = number // 10
        summ += num
    if (summ % 7) == 0:
        summ_var_a += cube_list[i]
print(summ_var_a)

# Вариант б) со одной зведочкой
for i in range(len(cube_list)):
    cube_list[i] += 17
    summ = 0
    number = cube_list[i]
    while number > 0:
        num = number % 10
        number = number // 10
        summ += num
    if (summ % 7) == 0:
        summ_var_b += cube_list[i]
print(summ_var_b)
