from tkinter import Tk, Frame

from typing import Callable

class Window(Tk):
    
    def __init__(self) -> None:
        super().__init__()
        self.frameStack = []
        self.FRAME_CHANGED_EVENT = "<<FrameChangeEvent>>"
        
    def setDefaultFrame(self, defaultFrame : Frame) -> None:
        self.frameStack = [defaultFrame]
        self.__changeFrame(nextFrame=defaultFrame)
        
    def __triggerFrameChangedEvent(self) -> None:
        self.event_generate(self.FRAME_CHANGED_EVENT)
        
    def bindForFrameChange(self, event : Callable) -> None:
        self.bind(self.FRAME_CHANGED_EVENT, event)
    
    def __changeFrame(self,  nextFrame : Frame, currentFrame : Frame = None) -> None:
        if currentFrame != None:
            currentFrame.pack_forget()
        nextFrame.pack()
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