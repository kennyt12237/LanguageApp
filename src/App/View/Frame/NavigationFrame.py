from tkinter import Frame, Button, Label, W

from ..Window import Window

class NavigationFrame(Frame):
        
    def __init__(self, window : Window, name : str = "Navigation") -> None:
        super().__init__(window, width=window.getWidthMinusPadding(), height=int(window.getHeight() * 0.2))
        self.window : Window = window
        self.name = name
        self.window.bindForFrameChange(self.onFrameChanged)
        self.backButton = Button(self, text="<-", command=self.backButtonPressed)
        self.frameLabel = Label(self, font=("Arial", 18))
        self.frameLabel.grid(row=0, column=1, pady=50, sticky=W)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.grid_propagate(False)
        
    def onFrameChanged(self, event) -> None:
        currentFrame = self.window.getCurrentFrame()
        self._newFrameNavigated(currentFrame)
    
    def __determineBackButtonChange(self) -> None:
        if self.window.getNumberOfFramesNavigated() == 1:
            self.backButton.grid_forget()
            return
        self.backButton.grid(row=0, column=0, sticky=W)

    def __setFrameHeader(self, frame : Frame) -> None:
        self.frameLabel.config(text=frame.winfo_name().capitalize())
        
    def setDefaultFrame(self, defaultFrame : Frame) -> None:
        self.__setFrameHeader(defaultFrame)
        
    def _newFrameNavigated(self, nextFrame : Frame) -> None:
        self.__determineBackButtonChange()
        self.__setFrameHeader(nextFrame)
       
    def backButtonPressed(self) -> None:
        self.window.returnToPreviousFrame()