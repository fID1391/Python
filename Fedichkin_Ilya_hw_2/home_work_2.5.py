# Федичкин Илья Дмитриевич
# Факультет Python-разработки
# Основы языка Python
# Lesson 2 task 5


price_list = [57.7, 86, 46.51, 97, 10345.52, 48.15, 53.4, 83.05, 91.16, 1999.09, 204.37, 502, 170.44, 703.99, 1400.23]

def to_fixed(num_obj):
    str_obj = f"{num_obj:.{2}f}"
    str_obj = f"{str_obj[:-3]} руб {str_obj[-2:]} коп, "
    return str_obj


def human_type(price_list):
    price_string = ''
    for index, price in enumerate(price_list, 0):
        price_string += to_fixed(price)
        if index == len(price_list) - 1:
            price_string = price_string[:-2] + '.'
    return print(price_string)


human_type(price_list)
print(id(price_list))

price_list.sort()
human_type(price_list)
print(id(price_list))


price_list_reverse = price_list.copy()
price_list_reverse.reverse()
human_type(price_list_reverse)
print(id(price_list_reverse))

# В задании под литерой D явно не указан тип и способ вывода цен, должен ли это быть список или строка через запятую или с рублями и копейками. Сделал несколько вариантов.
# Вариант 1.
human_type(price_list[-5:])


# Вариант 2.
print(price_list_reverse[4::-1])

# Вариант 3.

print(', ' .join(map(str, price_list[-5:])))

# Вариант 4.
print(str(price_list[-5:]).strip('[]'))
