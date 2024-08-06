from tkinter import Frame
from typing import Callable
import ctypes

from .Frame import NavigationFrame, HomeFrame
from .Window import Window
from .Utils import packAllChildWidgets

class BasicView():
    
    def __init__(self, window : Window = Window(), windowsize : float = 0.5, scaling : float = 2):
        self.window : Window = window
        self._setWindowSize(windowsize)
        self._setWidgetScaling(scaling)
        self.navigationFrame = NavigationFrame(self.window)
        self.homeFrame = HomeFrame(self.window)
        self._setDefaultFrame(self.homeFrame)
        packAllChildWidgets(self.window)
        
    def mainloop(self) -> None:
        self.window.mainloop()
        
    def _setWidgetScaling(self, factor : float) -> None:
        self.window.call("tk", 'scaling', 2)
        
    def _setWindowSize(self, percentage : float) -> None:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
        adjusted_width = int(screen_width * percentage)
        adjusted_height = int(screen_height * percentage)
        self.window.geometry("{width}x{height}".format(width = adjusted_width, height=adjusted_height))
        
    def _setDefaultFrame(self, defaultFrame : Frame) -> None:
        self.navigationFrame.setDefaultFrame(defaultFrame)
        self.window.setDefaultFrame(defaultFrame)
        
    def attachToDictionaryButton(self, method : Callable) -> None:
        self.homeFrame.setGetDictionaryData(method)
    
    def attachToSectionButton(self, method : Callable) -> None:
        self.homeFrame.setGetSectionsData(method)