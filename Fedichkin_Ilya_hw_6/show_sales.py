import sys

args = sys.argv[1:]


def read_sales(arg):
    if len(arg) > 2:
        return print('Неверный ввод данных')
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for index, line in enumerate(f, 1):
            if arg:
                if len(arg) == 2 and int(args[0]) <= index <= int(args[1]):
                    print(line.strip())
                elif len(arg) == 1 and int(args[0]) <= index:
                    print(line.strip())
            else:
                print(line.strip())


read_sales(args)
