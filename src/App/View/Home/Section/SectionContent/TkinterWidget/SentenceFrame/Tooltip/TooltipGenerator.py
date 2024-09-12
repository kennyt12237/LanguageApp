from tkinter import Misc
from .Widget import TooltipLabel


class TooltipGenerator():

    DEFAULT_TOOLTIP_TEXT = "tooltip"

    def __init__(self, labelName: str = DEFAULT_TOOLTIP_TEXT, startingNumber: int = 0):
        self.labelName = labelName
        self.number = startingNumber

    def createTooltipLabel(self, master: Misc, tooltipParent: Misc, **kwargs) -> TooltipLabel:
        tooltipName = self.DEFAULT_TOOLTIP_TEXT + str(self.__getNumber())
        self.__incrementNumber()
        return self._createTooltipLabel(master, tooltipParent, tooltipName=tooltipName, **kwargs)

    def __incrementNumber(self) -> None:
        self.number += 1

    def __getNumber(self) -> int:
        return self.number

    def _createTooltipLabel(self, master: Misc, tooltipParent: Misc, tooltipName: str, **kwargs):
        return TooltipLabel(master, tooltipParent, tooltipName=tooltipName, **kwargs)
