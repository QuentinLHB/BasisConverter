
class Decimal:

    def __init__(self, nb):
        self.__nb = nb

    def toBinary(self):
        b10 = self.__nb
        b2 = ""
        while b10 != 1:
            b2 = str(b10 % 2) + b2  # ajout du reste reste
            b10 = b10 // 2  # div
        return "1" + b2

    def toHexadecimal(self):
        b10 = self.__nb
        b16 = ""

        while b10 >= 16:
            b16 = Decimal.B16Equivalent(b10 % 16) + b16
            b10 = b10 // 16

        return Decimal.B16Equivalent(int(b10)) + b16


    @staticmethod
    def B16Equivalent(b10):
        if 10 <= b10 <= 15:
            return chr(b10+55)
        else :
            return str(b10)
