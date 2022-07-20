class Cell:

    def __init__(self, cell_number):
        if isinstance(cell_number, int):
            self.cell_number = cell_number
        else:
            raise ValueError('Количество ячеек не является целым')

    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.cell_number + other.cell_number)

    def __sub__(self, other):
        if isinstance(other, Cell) and self.cell_number > other.cell_number:
            return Cell(self.cell_number - other.cell_number)
        raise ValueError(f"Ошибка вычитания: {self.cell_number} <= {other.cell_number}")

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.cell_number * other.cell_number)

    def __truediv__(self, other):
        if isinstance(other, Cell):
            return Cell(self.cell_number // other.cell_number)

    def make_order(self, columns):
        solid = self.cell_number // columns
        remain = self.cell_number % columns
        return ("*"*columns + "\n")*solid + "*"*remain + "\n"


c1 = Cell(28)
c2 = Cell(12)
print(c1.make_order(7))
print(c2.make_order(7))

c3 = c1-c2
print(c3.make_order(7))
c4 = Cell(28.5)
