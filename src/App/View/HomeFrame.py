from tkinter import Frame, Button
from .WidgetUtils import packAllChildWidgets, packForgetAllChildWidgets
from .DictionaryFrame import DictionaryFrame
from .SectionFrame import SectionFrame
from typing import Callable


class HomeFrame(Frame):
    
    def __init__(self, window, changeFrame = None):
        super().__init__(window)
        self.changeFrame = changeFrame
        self.getDictionaryData : Callable = None
        self.getSectionsData : Callable = None
        self.dictionaryButton = Button(self, text="Dictionary", command=self.onDictionaryButtonPressed)
        self.sectionsButton = Button(self, text="Sections", command=self.onSectionsButtonPressed)
        
    def setGetDictionaryData(self, method : Callable) -> None:
        self.getDictionaryData = method
        
    def onDictionaryButtonPressed(self) -> None:
        if self.changeFrame:
            parent = self.master
            self.changeFrame(DictionaryFrame(parent, self.getDictionaryData())) if self.getDictionaryData else self.changeFrame(DictionaryFrame(parent))
    
    def setGetSectionsData(self, method : Callable) -> None:
        self.getSectionsData = method
        
    def onSectionsButtonPressed(self) -> None:
        if self.changeFrame:
            parent = self.master
            self.changeFrame(SectionFrame(parent, self.getSectionsData())) if self.getSectionsData else self.changeFrame(SectionFrame(parent))
            
    def pack(self) -> None:
        packAllChildWidgets(self)
        super().pack()
        
    def pack_forget(self) -> None:
        packForgetAllChildWidgets(self)
        super().pack_forget()