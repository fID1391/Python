def val_checker(x):
    def _val_checker(func):
        def wrapper(*args):
            try:
                for arg in args:
                    if arg < 1:
                        raise ValueError
            except ValueError:
                return print(f'ValueError: wrong val {arg}')
            return func(arg)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
