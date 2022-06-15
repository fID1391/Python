import re


list_val = []
tuples_data_list = []
counter_1 = 0
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        counter_1 += 1
        list_val.clear()
        line.strip()
        list_val.append(line[:line.find(' ')])
        list_val.append(re.findall('\"\w+\s\B', line)[0][1:-1])
        list_val.append(re.findall('\/\w+\/\w+\d\s', line)[0].strip())
        tuples_data_list.append(tuple(list_val))
print(counter_1)
print(len(tuples_data_list))
