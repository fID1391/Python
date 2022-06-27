"""
Реализовать базовый класс Worker (работник).
    определить атрибуты:
        -name,
        -surname,
        -position (должность),
        -income (доход);
        последний атрибут должен быть защищённым и ссылаться на словарь,
        содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};

создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения
    -полного имени сотрудника (get_full_name) и
    -дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных:
создать экземпляры класса Position,
передать данные, проверить значения атрибутов,
вызвать методы экземпляров."""


class Worker:
    __INCOME = {'manager': {'wage': 10000, 'bonus': 50000},
                'hr_manager': {'wage': 20000, 'bonus': 50000},
                'developer': {'wage': 100000, 'bonus': 0}
                }

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = self.__INCOME[position]

    def get_info(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nДолжность: {self.position}'


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["bonus"]}'


worker_1 = Position('Ilya', 'Fedichkin', 'developer')
print(worker_1.get_full_name())
print(worker_1.get_total_income())

worker_2 = Position('Ivan', 'Ivanov', 'manager')
print(worker_2.get_full_name())
print(worker_2.get_total_income())

worker_3 = Position('Aleks', 'Parabuchev', 'hr_manager')
print(worker_3.get_full_name())
print(worker_3.get_total_income())

print(worker_3.get_info())
