from itertools import zip_longest


def tup_gen(name, klass):
    """

    :param name: list of tutor's names
    :param klass: list of classes
    :return: tuple of name and class
    """
    if len(name) <= len(klass):
        for name, klass in zip(name, klass):
            yield name, klass
    else:
        for name, klass in zip_longest(name, klass):
            yield name, klass


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

gen_tut_klass = tup_gen(tutors, klasses)
print(next(gen_tut_klass))
print(next(gen_tut_klass))
print(next(gen_tut_klass))
print(next(gen_tut_klass))
print(next(gen_tut_klass))
print(next(gen_tut_klass))
print(next(gen_tut_klass))
print(next(gen_tut_klass))
print(next(gen_tut_klass))
print(next(gen_tut_klass))
print(next(gen_tut_klass))
print(next(gen_tut_klass))



