"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""


class Matrix:

    def __init__(self, lst):
        if self.__is_init_data_valid(lst):
            self.data = lst
        else:
            raise ValueError("Incorrect data for Matrix initialization: not equal lenght of lists")

    @staticmethod
    def __is_init_data_valid(data):
        set_lenght = {len(lst) for lst in data}
        if len(set_lenght) == 1:
            return True
        else:
            return False

    @property
    def dim(self):
        return len(self.data), len(self.data[0])

    def __str__(self):
        rez = ""
        for row in self.data:
            rez += "| "
            for element in row:
                rez += f"{element:3d} "
            rez += "|\n"
        return rez

    def __add__(self, other):
        if self.dim != other.dim:
            raise ValueError("Incorrect dimensions for add method")
        new_list = []
        for idx, row in enumerate(self.data):
            new_row = []
            for jdx, el in enumerate(row):
                new_row.append(self.data[idx][jdx] + other.data[idx][jdx] )
            new_list.append(new_row)
        return Matrix(new_list)


m1 = Matrix([[11, 2, 3], [4, 5, 6], [98, 8, 9]])
m2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
m3 = Matrix([[1, 1], [1, 1], [1, 1]])
m4 = m1 + m2
print(m4)
m5 = m1 + m3

print(m5)

m3 = Matrix([[1, 1, 1, 1], [1, 1, 1], [1, 1, 1]])




