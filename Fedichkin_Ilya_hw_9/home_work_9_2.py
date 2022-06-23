

def validation_float(msg):
    while True:
        value = input(f'{msg}')
        try:
            value = float(value)
            break
        except ValueError:
            print('Введенное значение не является числом.')
    return value


class Road:
    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width
        self.__mass_of_layer = 25
        print(f'Объект класса Road создан')

    def info(self):
        val = 5

    def mass_of_asphalt(self, thin_of_layer: float):
        mass_of_asphalt = self.__length * self.__width * self.__mass_of_layer * thin_of_layer
        print(f'Масса асфольта для покрытия участка дороги площадью'
              f' {self.__width * self.__length} м^2 равна: {mass_of_asphalt} кг.')


if __name__ == '__main__':
    length_of_road = validation_float('Введите длину участка трассы, [м]: ')
    width_of_road = validation_float('Введите ширину участка трассы, [м]: ')
    my_road = Road(length_of_road, width_of_road)
    thin_layer = validation_float('Введите толщину слоя участка трассы, [см]: ')
    my_road.mass_of_asphalt(thin_layer)
