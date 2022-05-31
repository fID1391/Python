# Федичкин Илья Дмитриевич
# Факультет Python-разработки
# Основы языка Python
# Lesson 3 task 1,2

num_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шеть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
    }


def num_translate_adv(arg):
    if arg.lower() in num_dict:
        if arg.istitle():
            return f'Перевод "{arg}" с аглйиского будет: "{num_dict[arg.lower()].capitalize()}"'
        else:
            return f'Перевод "{arg}" с аглйиского будет: "{num_dict[arg]}"'
    return None


numeric = input('Введите числительное на аглийском языке от нуля до десяти включительно, чтобы увидеть перевод: ')
print(num_translate_adv(numeric))
