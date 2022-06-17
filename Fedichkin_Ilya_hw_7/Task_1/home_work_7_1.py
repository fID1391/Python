import os
from pathlib import Path


def dirs_from_dict(dirs_dict: dict, par_path=''):
    """
    Функция рекурсивно создает папки из словаря по следующей структуре: любой ключ словаря является папкой, если значение словаря
    является словарем, создается подпапка.
    :param dirs_dict: словарь заданной структуры
    :param par_path: путь родительской папки формата os.path.abspath(os.curdir)
    :return: ничего не возвращает
    """
    for key, val in dirs_dict.items():
        p = Path(f'{par_path}/{key}')
        p.mkdir(parents=True, exist_ok=True)
        if isinstance(val, dict):
            dirs_from_dict(val, f'{par_path}/{key}')


my_proj = {'my_project': {'settings': {'video': ['None'],
                                       'audio': 'None'},
                          'mainapp': None,
                          'adminapp': None,
                          'authapp': None
                          }
           }

dir_ = os.path.abspath(os.curdir)

dirs_from_dict(my_proj, dir_)
