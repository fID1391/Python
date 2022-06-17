import os

dir = 'some_data'
interval = [100, 1000, 10000, 100000]
result = dict.fromkeys(interval, 0)

for address, dirs, files in os.walk(dir):
    for file in files:
        path = os.path.join(address, file)
        size = os.path.getsize(path)

        group = min(filter(lambda x: size < x, interval))
        result[group] += 1

print(result)
