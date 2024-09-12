from tkinter import Misc
from .TooltipLabel import TooltipLabel

class WordTooltipLabel(TooltipLabel):

    def __init__(self, master: Misc, tooltipParent: Misc, **kwargs) -> None:
        super().__init__(master, tooltipParent, **kwargs)

    def _setText(self, data) -> None:
        text = "Pinyin : {pinyin}\nCharacter : {character}\nType : {type}\nMeaning : {meaning}".format(
            pinyin=data["pinyin"],
            character=data["character"],
            type=data["type"],
            meaning=data["meaning"])
        self.toolTip.configure(text=text)