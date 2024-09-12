from tkinter import Misc

from .TooltipGenerator import TooltipGenerator
from .Widget import WordTooltipLabel


class WordTooltipGenerator(TooltipGenerator):
    
    WORD_LABEL_TOOLTIP = "wltooltip"
    
    def __init__(self, labelName : str = WORD_LABEL_TOOLTIP) -> None:
        super().__init__(labelName=labelName)
        
    def _createTooltipLabel(self, master: Misc, tooltipParent: Misc, tooltipName: str, **kwargs):
        return WordTooltipLabel(master, tooltipParent, tooltipName=tooltipName, **kwargs)