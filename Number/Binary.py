from Number.Decimal import Decimal


class Binary:

    def __init__(self, nb):
        self.__nb = nb

    def toDecimal(self):
        b2 = self.__nb
        b10 = 0
        n = 0
        while b2 != "":
            last = len(b2) - 1
            bit = int(b2[last:])
            b10 += bit * pow(2, n)
            n += 1
            b2 = b2[0:last]
        return b10

    def toHexadecimal(self):
        return Decimal(self.toDecimal()).toHexadecimal()

    @staticmethod
    def isBinary(number: int):
        return number == 0 or number == 1
