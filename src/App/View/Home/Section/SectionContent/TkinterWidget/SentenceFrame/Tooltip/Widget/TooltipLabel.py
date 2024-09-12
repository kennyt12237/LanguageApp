from tkinter import Misc
from tkinter.font import Font
from tkinter import DISABLED
from .KLabel import KLabel

from abc import ABC, abstractmethod

class TooltipLabel(ABC, KLabel):

    ENTER_SEQUENCE = "<Enter>"
    LEAVE_SEQUENCE = "<Leave>"

    def __init__(self, master: Misc, tooltipParent: Misc, tooltipName: str, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.tooltipParent = tooltipParent
        self.toolTip: KLabel = KLabel(self.tooltipParent, name=tooltipName, borderwidth=2,
                                      padx=10, pady=10, relief="solid", background="lightyellow")
        self.toolTip.event_generate(self.WIDGET_CREATED_EVENT)

    def setToolTip(self, data) -> None:
        self.bind(self.ENTER_SEQUENCE, func=lambda e: self.__setTooltipText(
            data))
        self.bind(self.LEAVE_SEQUENCE, func=lambda e: self.__hideToolTip())

    def __setTooltipText(self, data) -> None:
        self._setText(data)
        if self.toolTip.cget("state") != DISABLED:
            toolTipfont = Font(font=self.cget("font"))
            toolTipWidth = toolTipfont.measure(self.cget("text"))
            xPos = self.master.winfo_x() + self.winfo_x() + int(toolTipWidth / 2) - \
                (self.toolTip.winfo_reqwidth() / 2)
            yPos = self.tooltipParent.winfo_height() - self.master.winfo_height() - \
                self.toolTip.winfo_reqheight() - 20
            self.toolTip.place(x=xPos, y=yPos)

    @abstractmethod
    def _setText(self, data) -> KLabel:
        pass

    def __hideToolTip(self) -> None:
        self.toolTip.place_forget()