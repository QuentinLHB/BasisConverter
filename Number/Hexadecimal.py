from Number.Decimal import Decimal


class Hexadecimal:

    def __init__(self, nb):
        self.__nb = nb

    def toDecimal(self):
        b16 = self.__nb
        b10 = 0
        n = 0
        while b16 != "":
            last = len(b16) - 1
            bit = Hexadecimal.B10Equivalent(b16[last:])
            b10 += bit * pow(16, n)
            n += 1
            b16 = b16[0:last]
        return b10

    def toBinary(self):
        return Decimal(self.toDecimal()).toBinary()

    @staticmethod
    def B10Equivalent(b16):
        try:
            b10 = int(b16)
            return b10
        except:
            if (ord(b16) >= ord("A") & ord(b16) <= ord("F")):
                return ord(b16) - 55  # ASCII of A = 65, 65-55 = 10
            else:
                return 0
