from tkinter import Tk, Frame

from typing import Callable

from ..Utils import getScreenWidthCtypes, getScreenHeightCtypes

class Window(Tk):
    
    def __init__(self, padx : int = 0, pady : int = 0) -> None:
        super().__init__()
        self.padx = padx
        self.pady = pady
        self.frameStack = []
        self.FRAME_CHANGED_EVENT = "<<FrameChangeEvent>>"
        self.adjustedWidth = getScreenWidthCtypes()
        self.adjustedHeight = getScreenHeightCtypes()
        self.grid_propagate(False)
        self.config(padx=padx, pady=pady, background="blue")
        
    def setDefaultFrame(self, defaultFrame : Frame) -> None:
        self.frameStack = [defaultFrame]
        
    def __triggerFrameChangedEvent(self) -> None:
        self.event_generate(self.FRAME_CHANGED_EVENT)
        
    def bindForFrameChange(self, event : Callable) -> None:
        self.bind(self.FRAME_CHANGED_EVENT, event)
    
    def __changeFrame(self,  nextFrame : Frame, currentFrame : Frame = None) -> None:
        if currentFrame != None:
            currentFrame.grid_forget()
        nextFrame.grid(row=1,column=0)
        nextFrame.grid_propagate(False)
        self.__triggerFrameChangedEvent()
        
    def newFrameNavigated(self, newFrame : Frame) -> Frame:
        currentFrame = self.getCurrentFrame()
        self.frameStack.append(newFrame)
        self.__changeFrame(nextFrame=newFrame, currentFrame=currentFrame)
        
    def returnToPreviousFrame(self) -> Frame:
        currentFrame = self.frameStack.pop()
        previousFrame = self.getCurrentFrame()
        self.__changeFrame(nextFrame=previousFrame, currentFrame=currentFrame)
        
    def getNumberOfFramesNavigated(self) -> int:
        return len(self.frameStack)
    
    def getCurrentFrame(self) -> Frame:
        return self.frameStack[-1]
    
    def setGeometry(self, newWidth : int, newHeight : int) -> None:
        self.adjustedWidth = newWidth
        self.adjustedHeight = newHeight
        self.geometry("{width}x{height}".format(width = newWidth, height=newHeight))
    
    def getWidth(self) -> int:
        return self.adjustedWidth
    
    def getHeight(self) -> int:
        return self.adjustedHeight
    
    def setWindowPadding(self, padx : int, pady : int) -> None:
        self.padx = padx
        self.pady = pady
        self.config(padx=padx, pady=pady)
        
    def getPaddingInfo(self) -> tuple:
        return self.padx, self.pady
    
    def getWidthMinusPadding(self) -> int:
        return self.adjustedWidth - (self.padx * 2)
    
    def getHeightMinusPadding(self) -> int:
        return self.adjustedHeight - (self.pady * 2)