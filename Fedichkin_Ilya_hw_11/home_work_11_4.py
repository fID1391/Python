
class ComplexNumber:
    def __init__(self, re, im):
        self.__re = re
        self.__im = im

    def __str__(self):
        rez = ""
        if self.__re !=0:
            rez += f"{self.__re}"
        if self.__im > 0:
            rez += f"+{self.__im}j"
        elif self.__im < 0:
            rez += f"{self.__im}j"
        return rez

    def __add__(self, other):
        return ComplexNumber(self.__re + other.__re,
                             self.__im + other.__im )

    def __sub__(self, other):
        return ComplexNumber(self.__re - other.__re,
                             self.__im - other.__im )

    def __mul__(self, other):
        return ComplexNumber(self.__re*other.__re - self.__im*other.__im,
                             self.__re*other.__im + self.__im*other.__re )



c1 = ComplexNumber(2,3)
c2 = ComplexNumber(-1,-1)

print(f"Число 1: {c1}")
print(f"Число 2: {c2}")

c3 = c1+c2
c4 = c1-c2
c5 = c1*c2

print(f"Сложение: {c3}")
print(f"Вычитание: {c4}")
print(f"Умножение: {c5}")


