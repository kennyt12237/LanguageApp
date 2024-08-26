from tkinter import Frame
from typing import Callable

from .Frame import NavigationFrame, HomeFrame, Window, getScreenWidthCtypes, getScreenHeightCtypes, setProcessDpiAwareness2


class BasicView():

    def __init__(self, window: Window = Window(padx=40, pady=20), windowsize: float = 0.5, scaling: float = 2):
        self.window: Window = window
        setProcessDpiAwareness2()
        self._setWindowSize(windowsize)
        self._setWidgetScaling(scaling)

        self.navigationFrame = NavigationFrame(self.window)
        self.navigationFrame.grid(row=0, column=0, sticky="nsew")

        self.homeFrame = HomeFrame(self.window, name="home")
        self.homeFrame.grid(row=1, column=0, sticky="nsew")

        self._setDefaultFrame(self.homeFrame)

        self.window.grid_rowconfigure(0, weight=3)
        self.window.grid_rowconfigure(1, weight=10)
        self.window.grid_columnconfigure(0, weight=1)

    def mainloop(self) -> None:
        self.window.mainloop()

    def _setWidgetScaling(self, factor: float) -> None:
        self.window.call("tk", 'scaling', factor)

    def _setWindowSize(self, percentage: float) -> None:
        screenWidth = getScreenWidthCtypes()
        screenHeight = getScreenHeightCtypes()
        self.window.setGeometry(
            int(screenWidth * percentage), int(screenHeight * percentage))

    def _setDefaultFrame(self, defaultFrame: Frame) -> None:
        self.navigationFrame.setDefaultFrame(defaultFrame)
        self.window.setDefaultFrame(defaultFrame)

    def attachToDictionaryButton(self, method: Callable) -> None:
        self.homeFrame.setGetDictionaryData(method)

    def attachToSectionButton(self, method: Callable) -> None:
        self.homeFrame.setGetSectionsData(method)
