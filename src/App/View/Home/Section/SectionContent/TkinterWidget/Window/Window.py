from tkinter import Tk, Frame, Widget, Event

from typing import Callable

from ..AbstractFrame import GridFrame
from .Utils import getScreenWidthCtypes, getScreenHeightCtypes


class Window(Tk):

    def __init__(self, padx: int = 0, pady: int = 0) -> None:
        super().__init__()
        self.padx = padx
        self.pady = pady
        self.frameStack = []
        self.FRAME_CHANGED_EVENT = "<<FrameChangeEvent>>"
        self.adjustedWidth = getScreenWidthCtypes()
        self.adjustedHeight = getScreenHeightCtypes()
        self.config(padx=padx, pady=pady)
        self.widgetStyling : dict[str, dict] = {}
        self.bind("<Map>", lambda e : self.__onWidgetMapped(e))
            
    def setDefaultFrame(self, defaultFrame: GridFrame) -> None:
        self.frameStack = [defaultFrame]

    def __triggerFrameChangedEvent(self) -> None:
        self.event_generate(self.FRAME_CHANGED_EVENT)

    def bindForFrameChange(self, event: Callable) -> None:
        self.bind(self.FRAME_CHANGED_EVENT, event)

    def __changeFrame(self,  nextFrame: GridFrame, currentFrame: GridFrame) -> None:
        currentFrame.grid_remove()
        nextFrame.grid(row=1, column=0, sticky="nsew") 
        self.__removePlacedWidgets()
        self.__triggerFrameChangedEvent()
        
    def __removePlacedWidgets(self) -> None:
        for widget in self.place_slaves():
            widget.place_forget()
            for event in widget.bind():
                widget.unbind(event)

    def newFrameNavigated(self, newFrame: GridFrame) -> None:
        currentFrame = self.getCurrentFrame()
        self.frameStack.append(newFrame)
        self.__changeFrame(nextFrame=newFrame, currentFrame=currentFrame)

    def returnToPreviousFrame(self) -> Frame:
        currentFrame = self.frameStack.pop()
        previousFrame = self.getCurrentFrame()
        self.__changeFrame(nextFrame=previousFrame, currentFrame=currentFrame)

    def returnHome(self) -> Frame:
        previousFrame = self.frameStack.pop()
        homeFrame = self.frameStack[0]
        for num in range(1, len(self.frameStack)):
            self.frameStack.pop()
        self.__changeFrame(nextFrame=homeFrame, currentFrame=previousFrame)

    def getNumberOfFramesNavigated(self) -> int:
        return len(self.frameStack)

    def getCurrentFrame(self) -> Frame:
        return self.frameStack[-1]

    def setGeometry(self, newWidth: int, newHeight: int) -> None:
        self.adjustedWidth = newWidth
        self.adjustedHeight = newHeight
        self.geometry("{width}x{height}".format(
            width=newWidth, height=newHeight))

    def getWidth(self) -> int:
        return self.adjustedWidth

    def getHeight(self) -> int:
        return self.adjustedHeight

    def setWindowPadding(self, padx: int, pady: int) -> None:
        self.padx = padx
        self.pady = pady
        self.config(padx=padx, pady=pady)

    def addWidgetStyling(self, name : str, styling : dict = None) -> None:
        self.widgetStyling[name] = styling
        self.__setWidgetStyling(self)
        
    def __onWidgetMapped(self, event : Event) -> None:
        widget : Widget = event.widget
        name = widget.winfo_name()
        for key in self.widgetStyling.keys():
            if key in name:
                widget.configure(**self.widgetStyling[key])
        
    def __setWidgetStyling(self, child : Widget) -> None:
        reversedList = child.winfo_children()
        for child in reversedList:
            name = child.winfo_name()
            for key in self.widgetStyling.keys():
                if key in name:
                    child.configure(**self.widgetStyling[key])
            self.__setWidgetStyling(child)