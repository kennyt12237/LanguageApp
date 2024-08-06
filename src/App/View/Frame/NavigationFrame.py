from tkinter import Frame, Button, Label, LEFT, RIGHT

from ..Window import Window

class NavigationFrame(Frame):
        
    def __init__(self, window, name : str = "Navigation") -> None:
        super().__init__(window)
        self.window : Window = window
        self.name = name
        self.backButton = Button(self, text="<-", command=self.backButtonPressed)
        self.frameLabel = Label(self)
        self.frameLabel.grid(row=0, column=1)
        self.window.bindForFrameChange(self.onFrameChanged)
        
    def onFrameChanged(self, event) -> None:
        currentFrame = self.window.getCurrentFrame()
        self._newFrameNavigated(currentFrame)
    
    def __determineBackButtonChange(self) -> None:
        if self.window.getNumberOfFramesNavigated() == 1:
            self.backButton.grid_forget()
            return
        self.backButton.grid(row=0, column=0)

    def __setFrameHeader(self, frame : Frame) -> None:
        self.frameLabel.config(text=frame.getName())
        
    def setDefaultFrame(self, defaultFrame : Frame) -> None:
        self.__setFrameHeader(defaultFrame)
        
    def _newFrameNavigated(self, nextFrame : Frame) -> None:
        self.__determineBackButtonChange()
        self.__setFrameHeader(nextFrame)
       
    def backButtonPressed(self) -> None:
        self.window.returnToPreviousFrame()