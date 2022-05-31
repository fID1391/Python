# Федичкин Илья Дмитриевич
# Факультет Python-разработки
# Основы языка Python
# Lesson 3 task 3,4


def thesaurus(*args):
    """ Form a dictionary from tuple of names with:

    key -- is the first letter of name
    value -- is the list of Names

    function supported repeated values


    """

    some_dict = {}
    for name in args:
        name = name.capitalize()
        some_dict.setdefault(name[0], [])
        some_dict[name[0]].append(name)

    return print(some_dict)


def thesaurus_2(*args):
    """ Form a dictionary from tuple of names with:

    key -- is the first letter of name
    value -- is the list of Names

    function doesn't support repeated values


    """
    some_dict = {}
    for name in args:
        name = name.capitalize()
        val = some_dict.setdefault(name[0], [name])
        if name not in val:
            some_dict[name[0]].append(name)

    return print(some_dict)





def thesaurus_adv(*args):
    """

        Создает словарь сотрудников с ключами по первым буквам фамилий, в которых находится словарь с ключами по первым буквам имен.
        На вход принимает кортеж из имен и фамилий (Имя Фамилия, Имя Фамилия)
        приводит имена и фамилии к записи с большой буквы

    """

    dict_sn = {}
    for args in sorted(args):
        name, surname = args.split(' ')
        name = name.capitalize()
        surname = surname.capitalize()
        args = f'{name} {surname}'
        sun_m_val = dict_sn.setdefault(surname[0], {name[0]: [args]})
        name_val = sun_m_val.setdefault(name[0], [args])
        if args not in name_val:
            name_val.append(args)
    return dict_sn


thesaurus('Игорь', 'Анна', 'Олег', 'Олег', 'Олег', 'Марфа', 'Олеся', 'иван', 'ЕВПАТИЙ', 'ЕЛЕНА', 'Анна')
thesaurus_2('Игорь', 'Анна', 'Олег', 'Олег', 'Олег', 'Марфа', 'Олеся', 'иван', 'ЕВПАТИЙ', 'ЕЛЕНА', 'Анна')
print(thesaurus_adv('Иван Серов', 'иваН Кулебяка', 'Виктория Складчикова', 'Валентина сыромяткина', 'Игорь Крут', 'Ильяс Фомин', 'александра волочкова', 'ВЕНиАМИН Крузенштерн', 'ПЕТР Петренко'))

