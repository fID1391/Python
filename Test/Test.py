import os
from pathlib import Path
import pprint

def dirs_from_dict(object, par_path=''):
    """
    Функция рекурсивно создает папки из словаря по следующей структуре: любой ключ словаря является папкой, если значение словаря
    является словарем, создается подпапка.
    :param dirs_dict: словарь заданной структуры
    :param par_path: путь родительской папки формата os.path.abspath(os.curdir)
    :return: ничего не возвращает
    """
    if isinstance(object, str):
        with open(f'{value}', 'w'):
            pass
    if isinstance(object, dict):
        p = Path(f'{par_path}/{key}')
        p.mkdir(parents=True, exist_ok=True)
        for val in object.values():
            dirs_from_dict(val, f'{par_path}/{key}')
    elif
    for item in dirs_dict:
            if isinstance(item, dict):
                dirs_from_dict(item, f'{par_path}/{key}')
            elif isinstance(item, list):
                for value in item:
                    if isinstance(value, str):
                        with open(f'{value}', 'w'):
                            pass
                    else:

        elif isinstance(val, str):
            with open(f'{val}', 'w'):
                pass


my_proj = {'my_project': {'settings': ['__init__py', 'dev.py', 'proj.py'],
                          'main_app': ['__init__py', 'models.py', 'views.py',
                                       {'templates': {'main_app': ['base.html', 'index.html']}}],
                          'auth_app': ['__init__py', 'models.py', 'views.py',
                                       {'templates': {'auth_app': ['base.html', 'index.html']}}]}}

dir_ = os.path.abspath(os.curdir)

# dirs_from_dict(my_proj, dir_)
# pprint.pprint(my_proj)

