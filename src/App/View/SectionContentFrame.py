from tkinter import Frame, Button
from .WidgetUtils import packAllChildWidgets

class SectionContentFrame(Frame):
    
    def __init__(self, window, sectionContentData = None) -> None:
        super().__init__(window)
        self.data = sectionContentData
        self.wordButton = Button(self, text="Words")
        self.grammarButton = Button(self, text="Grammars")
        self.sentenceButton = Button(self, text="Sentences")
        
    def pack(self) -> None:
        packAllChildWidgets(self)
        super().pack()
        