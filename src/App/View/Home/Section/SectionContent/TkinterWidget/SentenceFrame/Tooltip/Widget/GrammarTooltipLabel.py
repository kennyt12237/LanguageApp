from tkinter import Misc
from .TooltipLabel import TooltipLabel

class GrammarTooltipLabel(TooltipLabel):

    def __init__(self, master: Misc, tooltipParent: Misc, tooltipName: str, **kwargs) -> None:
        super().__init__(master, tooltipParent, tooltipName, **kwargs)

    def _setText(self, data) -> None:
        text = "Pinyin : {pinyin}\nCharacter : {character}{num}\nMeaning : {meaning}".format(
            pinyin=data["pinyin"],
            character=data["character"],
            num=data["number"],
            meaning=data["usage"])
        self.toolTip.configure(text=text)