from tkinter import Frame, Button, Label
from ..Window import Window

class NavigationFrame(Frame):
        
    def __init__(self, window) -> None:
        super().__init__(window)
        self.window : Window = window
        self.backButton = Button(self, text="<-", command=self.backButtonPressed)
        self.frameLabel = Label(self)
        self.window.bindForFrameChange(self.onFrameChanged)
        
    def pack(self) -> None:
        self.frameLabel.pack()
        super().pack()
        
    def __packButton(self) -> None:
        self.backButton.pack()
        
    def __unpackButton(self) -> None:
        self.backButton.pack_forget()
        
    def onFrameChanged(self, event) -> None:
        currentFrame = self.window.getCurrentFrame()
        self._newFrameNavigated(currentFrame)
    
    def __determineBackButtonChange(self) -> None:
        if self.window.getNumberOfFramesNavigated() == 1:
            self.__unpackButton()
            return
        self.__packButton()

    def __setFrameHeader(self, frame : Frame) -> None:
        self.frameLabel.config(text=type(frame).__name__)
        
    def setDefaultFrame(self, defaultFrame : Frame) -> None:
        self.__setFrameHeader(defaultFrame)
        
    def _newFrameNavigated(self, nextFrame : Frame) -> None:
        self.__determineBackButtonChange()
        self.__setFrameHeader(nextFrame)
       
    def backButtonPressed(self) -> None:
        self.window.returnToPreviousFrame()