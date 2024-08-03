from .NavigationFrame import NavigationFrame
from .HomeFrame import HomeFrame
from .Window import Window

from tkinter import Frame
from .WidgetUtils import packAllChildWidgets

from typing import Callable
        
class BasicView():
    
    def __init__(self, window : Window = Window()):
        self.window : Window = window
        self.navigationFrame = NavigationFrame(self.window)
        self.homeFrame = HomeFrame(self.window)
        self._setDefaultFrame(self.homeFrame)
        # self.navigationFrame.setDefaultFrame(self.homeFrame)
        # self.navigationFrame.setFrameHeader(self.homeFrame)
        packAllChildWidgets(self.window)
        
    def mainloop(self) -> None:
        self.window.mainloop()
        
    def _setDefaultFrame(self, defaultFrame : Frame) -> None:
        self.window.setDefaultFrame(defaultFrame)
        self.navigationFrame.setDefaultFrame(defaultFrame)
        
    def attachToDictionaryButton(self, method : Callable) -> None:
        self.homeFrame.setGetDictionaryData(method)
    
    def attachToSectionButton(self, method : Callable) -> None:
        self.homeFrame.setGetSectionsData(method)