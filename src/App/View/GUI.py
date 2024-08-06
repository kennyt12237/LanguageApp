from tkinter import Frame
from typing import Callable
import ctypes

from .Frame import NavigationFrame, HomeFrame
from .Window import Window
from .Utils import packAllChildWidgets

class BasicView():
    
    def __init__(self, window : Window = Window()):
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        self.window : Window = window
        self.window.call("tk", 'scaling', '2')
        self.navigationFrame = NavigationFrame(self.window)
        self.homeFrame = HomeFrame(self.window)
        self._setDefaultFrame(self.homeFrame)
        packAllChildWidgets(self.window)

    def mainloop(self) -> None:
        self.window.mainloop()
        
    def _setDefaultFrame(self, defaultFrame : Frame) -> None:
        self.navigationFrame.setDefaultFrame(defaultFrame)
        self.window.setDefaultFrame(defaultFrame)
        
    def attachToDictionaryButton(self, method : Callable) -> None:
        self.homeFrame.setGetDictionaryData(method)
    
    def attachToSectionButton(self, method : Callable) -> None:
        self.homeFrame.setGetSectionsData(method)