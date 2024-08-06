from tkinter import Frame
from typing import Callable
import ctypes

from .Frame import NavigationFrame, HomeFrame
from .Window import Window
from .Utils import packAllChildWidgets, getScreenWidthCtypes, getScreenHeightCtypes, setProcessDpiAwareness2

class BasicView():
    
    def __init__(self, window : Window = Window(), windowsize : float = 0.5, scaling : float = 2):
        self.window : Window = window
        setProcessDpiAwareness2()
        self._setWindowSize(windowsize)
        self._setWidgetScaling(scaling)
        self.navigationFrame = NavigationFrame(self.window)
        self.homeFrame = HomeFrame(self.window)
        self._setDefaultFrame(self.homeFrame)
        packAllChildWidgets(self.window)
        self.window.setWindowPadding(20, 20)
        
    def mainloop(self) -> None:
        self.window.mainloop()
        
    def _setWidgetScaling(self, factor : float) -> None:
        self.window.call("tk", 'scaling', factor)
    
    def _setWindowSize(self, percentage : float) -> None:
        screenWidth = getScreenWidthCtypes()
        screenHeight = getScreenHeightCtypes()
        self.window.setGeometry(int(screenWidth * percentage),int(screenHeight * percentage))
    
    def _setDefaultFrame(self, defaultFrame : Frame) -> None:
        self.navigationFrame.setDefaultFrame(defaultFrame)
        self.window.setDefaultFrame(defaultFrame)
        
    def attachToDictionaryButton(self, method : Callable) -> None:
        self.homeFrame.setGetDictionaryData(method)
    
    def attachToSectionButton(self, method : Callable) -> None:
        self.homeFrame.setGetSectionsData(method)