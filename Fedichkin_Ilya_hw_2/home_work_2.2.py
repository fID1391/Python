# Федичкин Илья Дмитриевич
# Факультет Python-разработки
# Основы языка Python
# Lesson 2 task 2 (task 3 with *)

# Вариант 1
# Если в задании нет опечатки, и кавычки надо вставлять в лист в соседние ячейки, то решение следующее:

some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(some_list)
some_string = ''
check = False

for value in some_list:
    i = some_list.index(value)
    if some_list[i].isdigit():
        if not check:
            some_list[i] = some_list[i].zfill(2)
            some_list.insert(i, '"')
            check = True
            continue
        else:
            some_list.insert(i+1, '"')
            check = False
    if some_list[i].startswith('+'or '-') and (some_list[i])[1:].isdigit():
        if not check:
            some_list[i] = some_list[i].zfill(3)
            some_list.insert(i, '"')
            check = True
            continue
        else:
            some_list.insert(i + 1, '"')
            check = False
print(some_list)

for i in range(len(some_list)):
    if i == len(some_list) - 1:
        some_string += f'{some_list[i]}'
    elif some_list[i] == '"' and some_list[i-1].isalpha():
        some_string += f'{some_list[i]}'
    elif some_list[i] == '"' and some_list[i+1] == '"':
        some_string += f'{some_list[i]} '
    elif some_list[i].isdigit() or some_list[i].startswith('+' or '-') and (some_list[i])[1:].isdigit():
        some_string += f'{some_list[i]}'
    elif some_list[i] == '"' and some_list[i+1].isdigit() and not some_list[i].startswith('+' or '-'):
        some_string += f'{some_list[i]}'
    elif some_list[i] == '"' and some_list[i+1].isalpha() or some_list[i+1] == '"':
        some_string += f'{some_list[i]} '
    else:
        some_string += f'{some_list[i]} '
print(some_string)


# Вариант 2
# Если в задании все же опечатка и кавычками надо просто обособить числа, то решение следующее:

some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for n, i in enumerate(some_list, 0):
    if i.isdigit():
        i = f'"{i.zfill(2)}"'
    elif i.startswith('+' or '-') and i[1:].isdigit():
        i = f'"{i.zfill(3)}"'
    some_list[n] = i
some_string = (' '.join(some_list))
print(some_list)
print(some_string)
