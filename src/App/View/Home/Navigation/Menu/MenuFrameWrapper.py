from tkinter import Misc
from tkinter import RAISED
from .MenuFrame import MenuFrame
from .Setting import SettingFrame

from ...Section import GridFrame

class MenuFrameWrapper(GridFrame):

    def __init__(self, master: Misc, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.menuFrame = MenuFrame(self, **kwargs)
        self.settingFrame = SettingFrame(
            self.winfo_toplevel(), borderwidth=3, relief=RAISED)
        self.settingFrame.setOnClosedButtonPressed(lambda: (self.settingFrame.place_forget(
        ), self.menuFrame.grid(row=0, column=0, sticky="nsew")))
        self.menuFrame.setOnSettingsButtonPressed(self.onSettingButtonPressed)
        self._gridPlacement()

    def setOnHomeButtonPressed(self, command) -> None:
        self.menuFrame.setOnHomeButtonPressed(command)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)

    def onSettingButtonPressed(self) -> None:
        self.settingFrame.lift()
        xPos = self.winfo_x()
        yPos = self.winfo_y()
        _, _, x2, _ = self.bbox()

        def onMenuFrameWrapperConfigure() -> None:
            xPos = self.winfo_x()
            yPos = self.winfo_y()
            self.settingFrame.place_configure(x=xPos, y=yPos)
        self.bind("<Configure>", lambda e: onMenuFrameWrapperConfigure())
        self.settingFrame.place(x=xPos, y=yPos, width=x2)

    def setOnSettingsButtonPressed(self, command) -> None:
        self.menuFrame.setOnSettingsButtonPressed(command)

    def _gridPlacement(self) -> None:
        self.menuFrame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
    def hideButton(self, button: str) -> None:
        self.menuFrame.hideButton(button=button)

    def showButton(self, button: str) -> None:
        self.menuFrame.showButton(button=button)