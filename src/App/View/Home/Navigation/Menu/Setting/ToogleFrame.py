from tkinter import Misc, Label, Radiobutton, StringVar
from ....Section import GridFrame

from typing import Callable

class ToogleFrame(GridFrame):
    def __init__(self, master : Misc, **kwargs):
        super().__init__(master, **kwargs)
        stringVar = StringVar(value="On")
        self.on = LabeledRadioButton(self, labelText="On", radioVariable=stringVar, radioValue="On")
        self.off = LabeledRadioButton(self, labelText="Off", radioVariable=stringVar, radioValue="Off")
        self._gridPlacement()
        
    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
        
    def _gridPlacement(self) -> None:
        self.on.grid(row=0, column=0, sticky="nsew")
        self.off.grid(row=0, column=1, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
    
    def setOnRadioButtonPressed(self, command : Callable) -> None:
        self.on.setRadioButtonPressed(command=command)
        
    def setOffRadioButtonPressed(self, command : Callable) -> None:
        self.off.setRadioButtonPressed(command=command)
        
class LabeledRadioButton(GridFrame):
    
    def __init__(self, master : Misc, labelText : str, radioVariable : StringVar = None, radioValue : int = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.variable = radioVariable
        self.label = Label(self, text=labelText)
        self.radioButton = Radiobutton(self, variable=radioVariable, value=radioValue, command=self.__getRadioValue)
        self._gridPlacement()
        
    def setRadioButtonPressed(self, command : Callable) -> None:
        self.radioButton.configure(command=command)
        
    def __getRadioValue(self) -> str:
        return self.variable.get()
    
    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
        
    def _gridPlacement(self) -> None:
        self.radioButton.grid(row=0, column=0, sticky="nsew")
        self.label.grid(row=0, column=1, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
