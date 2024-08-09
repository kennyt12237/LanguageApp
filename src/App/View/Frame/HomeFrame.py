from tkinter import Button, Misc
from tkinter import CENTER
from typing import Callable

from .GridFrame import GridFrame
from .DictionaryFrame import DictionaryFrame
from .SectionFrame import SectionFrame
from ..Window import Window
from ..Utils import convertPixelsToTextUnit

class HomeFrame(GridFrame):
    
    def __init__(self, master : Misc, window : Window, name : str = "Home", defaultWidgetSize : float = 0.1):
        super().__init__(master, window, name, width=window.getWidthMinusPadding(), height=int(window.getHeight() * 0.5), background="green")
        self.defaultWidgetSize = defaultWidgetSize
        self.getDictionaryData : Callable = None
        self.getSectionsData : Callable = None
        self.dictionaryButton = Button(self, text="Dictionary", command=self.onDictionaryButtonPressed)
        self.sectionButton = Button(self, text="Sections", command=self.onSectionsButtonPressed)
        self.dictionaryButton.grid(row=0, column=0, pady=(0,20))
        self.sectionButton.grid(row=1,column=0)
        self.setWidgetSizeRelativeToScreen(defaultWidgetSize)
        
    def setWidgetSizeRelativeToScreen(self, relativeSize : float) -> None:
        widthSize = int(self.window.getWidth() * relativeSize)
        heightSize = int(self.window.getHeight() * relativeSize)
        self.setDictionaryButtonSize(widthSize, heightSize)
        self.setSectionButtonSize(widthSize, heightSize)
        
    def setGetDictionaryData(self, method : Callable) -> None:
        self.getDictionaryData = method
        
    def onDictionaryButtonPressed(self) -> None:
        self.window.newFrameNavigated(DictionaryFrame(self.window, self.window, self.getDictionaryData()))
    
    def setGetSectionsData(self, method : Callable) -> None:
        self.getSectionsData = method
        
    def onSectionsButtonPressed(self) -> None:
        self.window.newFrameNavigated(SectionFrame(self.window, self.window, self.getSectionsData()))
        
    def setDictionaryButtonSize(self, widthPixels : int, heightPixels : int) -> None:
        width, height = convertPixelsToTextUnit(self.dictionaryButton, widthPixels, heightPixels)
        self.dictionaryButton.config(width=width, height=height)

    def setSectionButtonSize(self, widthPixels : int, heightPixels : int) -> None:
        width, height = convertPixelsToTextUnit(self.sectionButton, widthPixels, heightPixels)
        self.sectionButton.config(width=width, height=height)
        
    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
        self.grid_anchor(CENTER)
