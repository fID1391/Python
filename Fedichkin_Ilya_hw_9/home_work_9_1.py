import time


class TrafficLight:
    def __init__(self):
        print('**Новый светофор создан**')
        self._color = ('Красный свет', 'Желтый свет', 'Зеленый свет')
        self._mode = 0
        self._tmd = (7, 2, 5)

    def running(self):
        print(f'Светофор запущен, сейчас {self._color[0]}')

    def stop(self):
        self._mode = 0
        print(f'Светофор выключен')

    def switch(self):
        if self._mode != 2:
            self._mode += 1
        else:
            self._mode = 0
        print(f'Светофор переключен на {self._color[self._mode]}')

    def auto_switch(self, arg=3):
        for ciles in range(arg):
            tdml = self._tmd[self._mode]
            tmdl_w = tdml
            while tmdl_w > 0:
                print(f'{self._color[self._mode]}. Осталось {tmdl_w} cек...')
                tmdl_w = tmdl_w - 1
                time.sleep(1)
            self.switch()
        print(f'Светофор остановлен, горит {self._color[self._mode]} свет.')


if __name__ == '__main__':
    new_trafficlight = TrafficLight()
    new_trafficlight.running()
    quit = False
    while not quit:
        user_control = input('1 - Ручное переключение\n'
                             '2 - Автоматическое переключение c 3 циклами\n'
                             'q - выход\n'
                             'Введите действие: ')
        if user_control == 'q':
            new_trafficlight.stop()
            break
        if len(user_control) == 1:
            try:
                mode = int(user_control)
                if mode == 1:
                    new_trafficlight.switch()
                elif mode == 2:
                    new_trafficlight.auto_switch()
            except ValueError:
                pass

    print('Выход из программы')

