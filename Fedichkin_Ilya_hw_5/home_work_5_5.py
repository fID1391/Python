from time import perf_counter


# Вариант 1. Неправильный с точки зрения производительности
def no_rep(arg: list):
    """Returns a list of non-duplicate values from the current list"""
    unique_numb = []
    temp = []
    for val in arg:
        if val not in temp and val not in unique_numb:
            unique_numb.append(val)
            temp.append(val)
        elif val in unique_numb and val in temp:
            unique_numb.remove(val)
    return unique_numb


# Вариант 2. Правльный с точки зрения производительности
def no_rep_2(arg: list):
    """Returns a list of non-duplicate values from the current list"""
    unique_numb = set()
    temp = set()
    for val in arg:
        if val not in temp:
            unique_numb.add(val)
        else:
            unique_numb.discard(val)
        temp.add(val)
    return [val for val in arg if val in unique_numb]


# для доказательства производительности генерируем следующий список
src = [val for val in range(2) for val in range(50000)]
src.append(10000002)
src.append(100000012)
src.append(10000002211)


start_1 = perf_counter()
print(no_rep(src))
stop_1 = perf_counter() - start_1
start_2 = perf_counter()
print(no_rep_2(src))
stop_2 = perf_counter() - start_2

print(stop_1, stop_2)
if stop_1 > stop_2:
    print('списки не рулят, от слова СОВСЕМ')
