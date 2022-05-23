# Федичкин Илья Дмитриевич
# Факультет Python-разработки
# Основы языка Python
# Lesson 1 task 3

# Вариант 1
n = 100
my_list = [str(i) for i in range(1, n+1)]
for i in range(len(my_list)):
    if str(my_list[i])[-2:] == ('11') or str(my_list[i])[-2:] == ('12') or str(my_list[i])[-2:] == ('13') or str(my_list[i])[-2:] == ('14'):
        my_list[i] += " процентов"
    elif str(my_list[i])[-1] == ('1'):
        my_list[i] += " процент"
    elif str(my_list[i])[-1] == ('2') or str(my_list[i])[-1] == ('3') or str(my_list[i])[-1] == ('4'):
        my_list[i] += " процента"
    else:
        my_list[i] += " процентов"
    print(my_list[i])

# Вариант 2
my_list_2 = list(str(i) for i in range(1, n+1))
for i in range(len(my_list_2)):
    if 11 <= int((my_list_2[i])[-2:]) <= 14:
        my_list_2[i] += " процентов"
    elif int((my_list_2[i])[-1:]) == 1:
        my_list_2[i] += " процент"
    elif 2 <= int((my_list_2[i])[-1:]) <= 4:
        my_list_2[i] += " процента"
    else:
        my_list_2[i] += " процентов"
    print(my_list_2[i])

# Вариант 3

for i in range(1, n+1):
    if 11 <= i % 100 <= 14:
        print("{} процентов".format(i))
    elif i % 10 == 1:
        print("{} процент".format(i))
    elif 2 <= i % 10 <= 4:
        print("{} процента".format(i))
    else:
        print("{} процентов".format(i))
