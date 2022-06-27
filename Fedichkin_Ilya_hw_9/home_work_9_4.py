"""
Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police=False):
        self.color = color
        self.user_speed = speed
        self.name = name
        self._is_police = is_police
        self._current_speed = 0
        self._direction = 'прямо'
        if self._is_police:
            self._max_speed = 200
        else:
            self._max_speed = 60

    def go(self):
        self._current_speed = self.user_speed
        return print(f'Автомобиль {self.name} начал движение со скоростью {self._current_speed}')

    def stop(self):
        self._current_speed = 0
        print(f'Автомобиль {self.name} остановлен')

    def turn(self, direction='прямо'):
        """Изменение напрвления движения автомобиля.

        :param direction: "прямо", "направо", "налево", "назад"
        :return: nothing
        """
        direction = direction.lower()
        if direction == 'прямо':
            print(f'Автомобиль {self.name} движется по прямой')
        elif direction == 'направо':
            print(f'Автомобиль {self.name} повернул направо')
        elif direction == 'налево':
            print(f'Автомобиль {self.name} повернул налево')
        elif direction == 'назад':
            print(f'Автомобиль {self.name} повернул в обратном направлении')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} равна {self._current_speed}')


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self._max_speed = 60

    def show_speed(self):
        if self._current_speed > self._max_speed:
            print(f'ВНИМАНИЕ! Превышен скоростной лимит. Текущая скорость {self._current_speed},'
                  f' ограниечение - {self._max_speed}')
        else:
            print(f'Текущая скорость {self._current_speed}, ограниечение - {self._max_speed}')


class SportCar(TownCar, Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self._max_speed = 90


class WorkCar(TownCar, Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self._max_speed = 40


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self._is_police = True


car1 = SportCar(120, 'Blue', 'Maserati')
car2 = WorkCar(60, 'White', 'Largus')
car3 = TownCar(80, 'Yellow', 'Solaris')

car1.user_speed = 120
car2.user_speed = 120
car2.user_speed = 120

car1.go()
car2.go()
car3.go()

car1.show_speed()
car2.show_speed()
car3.show_speed()

car4 = PoliceCar(120, 'Blue', 'Camry')
car4.go()

car4.show_speed()

car1.turn('Направо')
car2.turn('Налево')
car3.turn('прямо')
car4.turn('назад')


some_car = Car('as', 'sd', 'sd')