from tkinter import Widget, font
from math import floor

def packAllChildWidgets(widget : Widget) -> None:
    for child in widget.winfo_children():
        child.pack()

def packForgetAllChildWidgets(widget : Widget) -> None:
    for child in widget.winfo_children():
        child.pack_forget()
    
def convertPixelsToTextUnit(widget : Widget, widthPixel : int, heightPixel : int) -> tuple:
    widgetFont = font.Font(font=widget.cget("font"))
    charWidth = widgetFont.measure("0")
    charHeight = widgetFont.metrics("linespace")
    
    widthInTextUnit = int(floor(widthPixel / charWidth))
    heightInTextUnit = int(floor(heightPixel /  charHeight))
    
    return widthInTextUnit, heightInTextUnit