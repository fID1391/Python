# Федичкин Илья Дмитриевич
# Факультет Python-разработки
# Основы языка Python
# Lesson 3 task 5(var2)

from random import randrange
import copy

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
    elif not flag:
        var = lst[randrange(len(lst))]
    else:
        var = ''
    return var


def get_jokes(arg, flag=True, **kwargs):
    """

    :param arg: number of jokes
    :param flag: word uniqueness condition
    :param kwargs: lists of words
    :return: list of strings with random words from kwargs
    """
    joke_list = []
    kwargs = copy.deepcopy(kwargs)
    for i in range(arg):
        joke = (' ' .join([method(value, flag) for value in kwargs.values()]))
        if joke.strip():
            joke_list.append(joke)
        else:
            return joke_list
    return joke_list


print(get_jokes(7, True, nouns=nouns, adverbs=adverbs, adjectives=adjectives))
print(get_jokes(7, False, nouns=nouns, adverbs=adverbs, adjectives=adjectives))



