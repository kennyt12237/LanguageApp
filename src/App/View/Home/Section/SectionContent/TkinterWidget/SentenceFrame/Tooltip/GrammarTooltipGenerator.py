from tkinter import Misc

from .Widget import GrammarTooltipLabel
from .TooltipGenerator import TooltipGenerator

class GrammarTooltipGenerator(TooltipGenerator):
    
    GRAMMAR_LABEL_TOOLTIP = "gltooltip"
    
    def __init__(self, labelName : str = GRAMMAR_LABEL_TOOLTIP) -> None:
        super().__init__(labelName=labelName)
        
    def _createTooltipLabel(self, master: Misc, tooltipParent: Misc, tooltipName: str, **kwargs):
        return GrammarTooltipLabel(master, tooltipParent, tooltipName=tooltipName, **kwargs)