from tkinter import Frame, Button, Label
from .Window import Window

class NavigationFrame(Frame):
        
    def __init__(self, window, initFrame : Frame = None) -> None:
        super().__init__(window)
        self.window : Window = window
        self.backButton = Button(self, text="<-", command=self.backButtonPressed)
        self.frameLabel = Label(self)
        self.frameLabel.pack()
        
    def setFrameHeader(self, frame : Frame) -> None:
        self.frameLabel.config(text=type(frame).__name__)
        
    def newFrameNavigated(self, newFrame : Frame) -> None:
        if self.backButton.winfo_ismapped() == 0:
            self.backButton.pack()
        self.setFrameHeader(newFrame)
        
    def backButtonPressed(self) -> Frame:        
        self.frameLabel.config(text=type().__name__)
        if len(self.frameStack) == 1:
            self.backButton.pack_forget()