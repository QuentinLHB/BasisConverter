import tkinter as tk

from GUI import GUIConstants as const
from Number.Decimal import Decimal


class MainWindow():

    def __init__(self, root: tk.Tk):
        self.__root = root
        self.__frame = tk.Frame(self.__root, width=const.WINDOW_WIDTH, height=const.WINDOW_HEIGHT)
        self.initUI()

    # def test(self, event):
    #     print(event.char)

    def initUI(self):
        # General window config
        self.__root.title("Test")
        self.__root.geometry(f"{const.WINDOW_WIDTH}x{const.WINDOW_HEIGHT}")

        # Desc on top
        lblDesc = tk.Label(self.__root, text="Entrez un nombre dans une des zones pour le convertir.")
        lblDesc.pack()

        # Containers
        self.__frame.pack(expand=True)
        self.__frame.anchor(tk.CENTER)
        self.__frame.grid_rowconfigure(0, weight=1)
        self.__frame.grid_columnconfigure(0, weight=1)

        # Widgets:
        # StringVars
        # self.sv10 = tk.StringVar()
        # sv2 = tk.StringVar()
        # sv16 = tk.StringVar()

        r = 1
        # Base 10
        self.lblB10 = tk.Label(self.__frame, text="Decimal :")
        self.lblB10.grid(row=r, column=0, sticky=tk.E, padx=const.GRID_PADX, pady=const.GRID_PADY)
        self.entryB10 = tk.Entry(self.__frame)
        # validate=const.ENTRY_VALIDATION, validatecommand=lambda: self.entry_textChanged(self.entryB10))
        self.entryB10.bind('<KeyRelease>', self.entry_textChanged)
        self.entryB10.grid(row=r, column=1, columnspan=2, padx=const.GRID_PADX, pady=const.GRID_PADY)
        r += 1

        # Base 2
        self.lbl2 = tk.Label(self.__frame, text="Binary :")
        self.lbl2.grid(row=r, column=0, sticky=tk.E, padx=const.GRID_PADX, pady=const.GRID_PADY)
        self.entryB2 = tk.Entry(self.__frame)
        self.entryB2.grid(row=r, column=1, columnspan=2, sticky=tk.W, padx=const.GRID_PADX, pady=const.GRID_PADY)
        r += 1

        # Base 16
        self.lblB16 = tk.Label(self.__frame, text="Hexadecimal :")
        self.lblB16.grid(row=r, column=0, sticky=tk.E, padx=const.GRID_PADX, pady=const.GRID_PADY)
        self.entryB16 = tk.Entry(self.__frame)
        self.entryB16.grid(row=r, column=1, columnspan=2, sticky=tk.W, padx=const.GRID_PADX, pady=const.GRID_PADY)
        r += 1

        # OK Button
        self.btnOK = tk.Button(self.__frame, text="OK", padx=15)
        self.btnOK.grid(row=r, column=0, columnspan=2, padx=const.GRID_PADX, pady=const.GRID_PADY)

        # Events
        # self.btnOK.bind('<Button-1>', lambda e: self.calculate())
        self.entryB10.bind()

    def entry_textChanged(self, event):
        print("text changed")
        if (event.widget is self.entryB10):
            self.fromB10(event.char)
        elif event.widget is self.entryB16:
            print("not yet")

    def fromB10(self, newChar):
        if str(newChar).isnumeric():
            self._convertB10toB2andB16(int(self.entryB10.get()))

        elif str(newChar).isalpha:
            if self.isNeitherAlphaNorNum(newChar):
                if self.entryB10.get() != "":
                    self._convertB10toB2andB16(int(self.entryB10.get()))
            else:  # Letter...
                print(newChar)
                print(ord(newChar))
                self._deleteLastChar(self.entryB10)

    def _convertB10toB2andB16(self, b10):
        b10 = Decimal(b10)
        self.clearEntries(self.entryB2, self.entryB16)
        self.entryB2.insert(0, b10.toBinary())
        self.entryB16.insert(0, b10.toHexadecimal())

    def clearEntries(self, *entryWidgets: tk.Entry):
        for entry in entryWidgets:
            entry.delete(0, 'end')

    def printNaN(self, *entryWidgets: tk.Entry):
        for entry in entryWidgets:
            entry.delete(0, 'end')
            entry.insert(0, const.NaN)

    def _deleteLastChar(self, entry: tk.Entry):
        length = len(entry.get())
        entry.delete(length - 1, length)

    def isNeitherAlphaNorNum(self, character):
        return character == "" or ord(character) == const.ENTER_KEY
