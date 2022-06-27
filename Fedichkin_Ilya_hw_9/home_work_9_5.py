"""
Реализовать класс Stationery (канцелярская принадлежность):
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    def __init__(self, title: str):
        self._title = title

    def draw(self):
        print(f'Запуск отрисовки {self._title}')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка ручкой {self._title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка карандашом {self._title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка маркером {self._title}')


paintbrush = Stationery('Paintbrush')
pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

paintbrush.draw()
pen.draw()
pencil.draw()
handle.draw()