# Федичкин Илья Дмитриевич
# Факультет Python-разработки
# Основы языка Python
# Lesson 2 task 4

some_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for values in some_list:
    print('Привет, {}!'.format((values[values.rfind(' ')+1:]).capitalize()))
