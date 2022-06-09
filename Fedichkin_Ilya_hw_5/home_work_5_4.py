from time import perf_counter


def more_prev_1(arg: list):
    return [num for i, num in enumerate(arg, 0) if i != 0 and arg[i - 1] < num]


def more_prev_2(arg: list):
    return [b for a, b in zip(arg, arg[1:]) if a < b]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 77]
result = [12, 44, 4, 10, 78, 123]


start = perf_counter()
print(more_prev_1(src))
cnt1 = perf_counter()-start
print(cnt1)

start2 = perf_counter()
print(more_prev_2(src))
cnt2 = perf_counter()-start2
print(cnt2)


if cnt1 < cnt2:
    print('enumerate рулит')
else:
    print('zip рулит')
