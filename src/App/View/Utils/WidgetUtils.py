from tkinter import Widget

def packAllChildWidgets(widget : Widget) -> None:
    for child in widget.winfo_children():
        child.pack()

def packForgetAllChildWidgets(widget : Widget) -> None:
    for child in widget.winfo_children():
        child.pack_forget()