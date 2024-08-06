from tkinter import Frame, Button
from typing import Callable

from .DictionaryFrame import DictionaryFrame
from .SectionFrame import SectionFrame
from ..Window import Window
from ..Utils import packAllChildWidgets, packForgetAllChildWidgets


class HomeFrame(Frame):
    
    def __init__(self, window : Window):
        super().__init__(window)
        self.window = window
        self.getDictionaryData : Callable = None
        self.getSectionsData : Callable = None
        self.dictionaryButton = Button(self, text="Dictionary", command=self.onDictionaryButtonPressed)
        self.sectionsButton = Button(self, text="Sections", command=self.onSectionsButtonPressed)
        
    def setGetDictionaryData(self, method : Callable) -> None:
        self.getDictionaryData = method
        
    def onDictionaryButtonPressed(self) -> None:
        self.window.newFrameNavigated(DictionaryFrame(self.window, self.getDictionaryData()))
    
    def setGetSectionsData(self, method : Callable) -> None:
        self.getSectionsData = method
        
    def onSectionsButtonPressed(self) -> None:
        self.window.newFrameNavigated(SectionFrame(self.window, self.getSectionsData()))
            
    def pack(self) -> None:
        packAllChildWidgets(self)
        super().pack()
        
    def pack_forget(self) -> None:
        packForgetAllChildWidgets(self)
        super().pack_forget()