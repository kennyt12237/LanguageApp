
from tkinter import Misc, Button
from tkinter import GROOVE, SUNKEN
from ....Section import GridFrame

class SizeFrame(GridFrame):

    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

    def __init__(self, master: Misc, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.smallButton = Button(self, text=self.SMALL, relief=GROOVE)
        self.mediumButton = Button(self, text=self.MEDIUM, relief=SUNKEN)
        self.largeButton = Button(self, text=self.LARGE, relief=GROOVE)
        self._gridPlacement()

    def _setGridProperties(self) -> None:
        pass

    def __setButtonSunkenAndRaisedRest(self, button: Button) -> None:
        button.configure(relief=SUNKEN)
        for cButton in self.winfo_children():
            if cButton != button:
                cButton.configure(relief=GROOVE)

    def setOnSmallButtonPressed(self, command) -> None:
        self.smallButton.config(command=lambda: (
            command(), self.__setButtonSunkenAndRaisedRest(self.smallButton)))

    def setOnMediumButtonPressed(self, command) -> None:
        self.mediumButton.config(command=lambda: (
            command(), self.__setButtonSunkenAndRaisedRest(self.mediumButton)))

    def setOnLargeButtonPressed(self, command) -> None:
        self.largeButton.config(command=lambda: (
            command(), self.__setButtonSunkenAndRaisedRest(self.largeButton)))

    def _gridPlacement(self) -> None:
        self.smallButton.grid(row=0, column=0, sticky="nsew")
        self.mediumButton.grid(row=0, column=1, sticky="nsew")
        self.largeButton.grid(row=0, column=2, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)