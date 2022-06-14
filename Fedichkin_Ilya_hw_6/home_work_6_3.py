from itertools import zip_longest


def cap_fun(arg):
    return [value.strip().capitalize() for value in arg]


users_dict = {}
with open('users.csv', 'r', encoding='utf-8') as file_1:
    with open('hobby.csv', 'r', encoding='utf-8') as file_2:
        for names, hobbyes in zip_longest(file_1, file_2, fillvalue='None'):
            users_dict.setdefault(names.rstrip(), hobbyes.rstrip())
with open('users_hobby.txt', 'w', encoding='utf-8') as file_3:
    for key, val in users_dict.items():
        if key != 'None':
            file_3.writelines(f'{key}: {val}\n')
        else:
            exit(1)
