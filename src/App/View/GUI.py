from .Frame import NavigationFrame, HomeFrame
from .Window import Window

from tkinter import Frame
from .Utils import packAllChildWidgets

from typing import Callable
import ctypes
        
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
        self.window.setDefaultFrame(defaultFrame)
        self.navigationFrame.setDefaultFrame(defaultFrame)
        
    def attachToDictionaryButton(self, method : Callable) -> None:
        self.homeFrame.setGetDictionaryData(method)
    
    def attachToSectionButton(self, method : Callable) -> None:
        self.homeFrame.setGetSectionsData(method)