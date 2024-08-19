from tkinter import Label, Misc
from .AbstractFrame import TableGridFrame
from .Styling import getTableHeaderLabelSettings, getTableLabelSettings
import json


class DictionaryFrame(TableGridFrame):

    def __init__(self, master: Misc, data: json = None, **kwargs):
        headerStyling = getTableHeaderLabelSettings()
        labelStyling = getTableLabelSettings()
        super().__init__(master, data, headerStyling, labelStyling, **kwargs)
