# Федичкин Илья Дмитриевич
# Факультет Python-разработки
# Основы языка Python
# Lesson 3 task 5

from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def method(lst, flag):
    """

    :param lst: list of words
    :param flag: True or False
    :return: .pop() of random value of list if True or random value of list if False


    """
    if flag and len(lst):
        var = lst.pop(randrange(len(lst)))
        return var
    elif not flag:
        var = lst[randrange(len(lst))]
        return var
    else:
        return ''


def get_jokes(arg, flag=True):
    """

    :param arg: number of jokes
    :param flag: word uniqueness condition
    :return: list of strings with jokes
    """
    non = nouns.copy()
    adv = adverbs.copy()
    adj = adjectives.copy()
    list_jokes = []
    for i in range(arg):
        joke = f'{method(non, flag)} {method(adv, flag)} {method(adj, flag)}'
        if joke.strip():
            list_jokes.insert(i, joke)
    return list_jokes


print(get_jokes(7, flag=False))

