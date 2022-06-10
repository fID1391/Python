n = 25
odd_num_var = (i for i in range(1, n + 1, 2))

for i in range(30):
    try:
        print(next(odd_num_var))
    except StopIteration:
        print('...StopIteration...')
        break

