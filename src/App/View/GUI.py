from .NavigationFrame import NavigationFrame
from .HomeFrame import HomeFrame
from .WidgetUtils import packAllChildWidgets

from tkinter import Frame, Tk
from typing import Callable

class BasicView():
    
    def __init__(self, tk : Tk = Tk()):
        self.window = tk
        self.navigationFrame = NavigationFrame(self.window)
        self.homeFrame = HomeFrame(self.window, self.changeFrame)
        self.navigationFrame.setDefaultFrame(self.homeFrame)
        self.navigationFrame.setFrameHeader(self.homeFrame)
        packAllChildWidgets(self.window)
        
    def mainloop(self) -> None:
        self.window.mainloop()
        
    def attachToDictionaryButton(self, method : Callable) -> None:
        self.homeFrame.setGetDictionaryData(method)
    
    def attachToSectionButton(self, method : Callable) -> None:
        self.homeFrame.setGetSectionsData(method)
        
    def changeFrame(self, newFrame : Frame) -> None:
        self.navigationFrame.newFrameNavigated(newFrame)