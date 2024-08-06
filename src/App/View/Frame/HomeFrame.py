from tkinter import Frame, Button
from typing import Callable

from .DictionaryFrame import DictionaryFrame
from .SectionFrame import SectionFrame
from ..Window import Window
from ..Utils import packAllChildWidgets, packForgetAllChildWidgets, convertPixelsToTextUnit

class HomeFrame(Frame):
    
    def __init__(self, window : Window, name : str = "Home", defaultWidgetSize : float = 0.1):
        super().__init__(window)
        self.window = window
        self.name = name
        self.defaultWidgetSize = defaultWidgetSize
        self.getDictionaryData : Callable = None
        self.getSectionsData : Callable = None
        self.dictionaryButton = Button(self, text="Dictionary", command=self.onDictionaryButtonPressed)
        self.sectionButton = Button(self, text="Sections", command=self.onSectionsButtonPressed)
        self.setWidgetSizeRelativeToScreen(defaultWidgetSize)
        
    def setWidgetSizeRelativeToScreen(self, relativeSize : float) -> None:
        widthSize = int(self.window.getWidth() * relativeSize)
        heightSize = int(self.window.getHeight() * relativeSize)
        self.setDictionaryButtonSize(widthSize, heightSize)
        self.setSectionButtonSize(widthSize, heightSize)
        
    def setGetDictionaryData(self, method : Callable) -> None:
        self.getDictionaryData = method
        
    def onDictionaryButtonPressed(self) -> None:
        self.window.newFrameNavigated(DictionaryFrame(self.window, self.getDictionaryData()))
    
    def setGetSectionsData(self, method : Callable) -> None:
        self.getSectionsData = method
        
    def onSectionsButtonPressed(self) -> None:
        self.window.newFrameNavigated(SectionFrame(self.window, self.getSectionsData()))

    def getName(self) -> None:
        return self.name
      
    def pack(self) -> None:
        packAllChildWidgets(self)
        super().pack()
        
    def pack_forget(self) -> None:
        packForgetAllChildWidgets(self)
        super().pack_forget()
        
    def setDictionaryButtonSize(self, widthPixels : int, heightPixels : int) -> None:
        width, height = convertPixelsToTextUnit(self.dictionaryButton, widthPixels, heightPixels)
        self.dictionaryButton.config(width=width, height=height)

    def setSectionButtonSize(self, widthPixels : int, heightPixels : int) -> None:
        width, height = convertPixelsToTextUnit(self.sectionButton, widthPixels, heightPixels)
        self.sectionButton.config(width=width, height=height)