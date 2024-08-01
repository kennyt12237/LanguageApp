from tkinter import Frame, Button, Label

class NavigationFrame(Frame):
        
    def __init__(self, window, initFrame:Frame = None) -> None:
        super().__init__(window)
        self.backButton = Button(self, text="<-", command=self.backButtonPressed)
        self.frameLabel = Label(self)
        self.frameLabel.pack()
        self.frameStack = []
        
        if initFrame: 
            self.setDefaultFrame(initFrame)
            self.setFrameHeader(self, initFrame)
    
    def setDefaultFrame(self, defaultFrame : Frame) -> None:
        self.frameStack = [defaultFrame]
        
    def setFrameHeader(self, frame : Frame) -> None:
        self.frameLabel.config(text=type(frame).__name__)
        
    def newFrameNavigated(self, newFrame : Frame) -> None:
        currentFrame = self.frameStack[-1]
        currentFrame.pack_forget()
        
        newFrame.pack()
        self.frameStack.append(newFrame)
        if self.backButton.winfo_ismapped() == 0:
            self.backButton.pack()
        self.setFrameHeader(newFrame)
        
    def backButtonPressed(self) -> Frame:
        # Remove Current Frame
        currentFrame = self.frameStack.pop()
        currentFrame.pack_forget()
        
        # Setting the current frame to the previous frame
        previousFrame = self.frameStack[-1]
        previousFrame.pack()
        self.frameLabel.config(text=type(previousFrame).__name__)
        if len(self.frameStack) == 1:
            self.backButton.pack_forget()
        return previousFrame
