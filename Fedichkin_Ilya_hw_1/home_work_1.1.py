# Федичкин Илья Дмитриевич
# Факультет Python-разработки
# Основы языка Python
# Lesson 1 task 1

while True:
    duration = input("Введите количество секунд для конвертации: ")
    if duration.isdigit():
        duration = int(duration)
        if duration > 0:
            break

seconds = duration % 60
minutes = (duration // 60) % 60
hours = (duration // 3600) % 24
days = (duration // 86400)

check_summ = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds

if check_summ == duration:
    if days > 0:
        print("{} дн. {} час. {} мин. {} сек." .format(days, hours, minutes, seconds))
    elif hours > 0:
        print("{} час. {} мин. {} сек.".format(hours, minutes, seconds))
    elif minutes > 0:
        print("{} мин. {} сек.".format(minutes, seconds))
    else:
        print("{} сек." .format(seconds))
else:
    print("Ошибка в коде!")