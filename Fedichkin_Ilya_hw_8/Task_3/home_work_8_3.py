

def type_logger(func):
    def wrapper(*args, **kwargs):
        res_args = (', '.join([f'{arg}: {type(arg)}' for arg in args]))
        res_kwargs = (', '.join([f'{key}= {value}: {type(value)}' for key, value in kwargs.items()]))
        print(f'function: {func.__name__}({res_args}, {res_kwargs})')
        new_args = []
        for ind, arg in enumerate(args):
            try:
                if isinstance(arg, int) or isinstance(arg, float):
                    new_args.append(arg)
                else:
                    raise ValueError
            except ValueError:
                print(f'ValueError: Value "{arg}" at index {ind} is not a number: {type(arg)}')
                continue
        new_args = tuple(new_args)
        new_kwargs = {}
        for key, value in kwargs.items():
            try:
                if isinstance(value, int) or isinstance(value, float):
                    new_kwargs.update({key: value})
                else:
                    raise ValueError
            except ValueError:
                print(f'ValueError: Value "{value}" at key "{key}" is not a number: {type(arg)}')
                continue
        type_mark = func(*new_args, **new_kwargs)
        return type_mark
    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    res_arg = [arg**3 for arg in args]
    res_kwarg = [val**3 for val in kwargs.values()]
    res_arg.extend(res_kwarg)
    return res_arg


print(calc_cube('5', (13, 12), 1, val=4, val2='5'))
