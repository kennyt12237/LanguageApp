from tkinter import Tk, Frame

class Window(Tk):
    
    def __init__(self) -> None:
        super().__init__()
        self.frameStack = []
        
    def setDefaultFrame(self, defaultFrame : Frame) -> None:        
        self.frameStack = [defaultFrame]
        self.__changeFrame(nextFrame=defaultFrame)
        
    def __changeFrame(self,  nextFrame : Frame, currentFrame : Frame = None) -> None:    
        if currentFrame != None:
            currentFrame.pack_forget() 
        nextFrame.pack()
        
    def _newFrameNavigated(self, newFrame : Frame) -> Frame:
        currentFrame = self.frameStack[-1]
        self.frameStack.append(newFrame)
        self.__changeFrame(nextFrame=newFrame, currentFrame=currentFrame)
        
    def _returnToPreviousFrame(self) -> Frame:
        self.frameStack.pop()
        previousFrame = self.framestack[-1]
        self.__changeFrame(nextFrame=previousFrame)