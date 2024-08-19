from tkinter import Label, Misc
from .GridFrame import GridFrame
import json


class TableGridFrame(GridFrame):

    NUMBER = "Number"
    GRID_STICKY = "nsew"
    GRID_BACKGROUND = "#d7f1f7"
    BG = "bg"
    HEADER_SIZE = 100
    ENTRY_SIZE = 75

    def __init__(self, master: Misc, data: json = None, headerStyling: dict[str, str] = {}, entryStyling: dict[str, str] = {}, **kwargs):
        super().__init__(master, **kwargs)
        self.data: list[dict[str, str]] = json.loads(data)
        self.__createLabels(self.data, headerStyling, entryStyling)

    def __createLabels(self, data: list[dict[str, str]], headerStyling: dict[str, str], entryStyling: dict[str, str]) -> None:
        headerItemCount = self._createHeader(
            data, numberColumn=True, headerStyling=headerStyling)
        labelCount = self._createEntries(
            data, labelCount=1, backgroundOnEven=True, entryStyling=entryStyling)
        self._additionalGridProperties(labelCount, headerItemCount)

    def _createHeader(self, data: list[dict[str, str]], numberColumn: bool = False, headerStyling: dict[str, str] = {}) -> int:
        headerList = list(data[0].keys())
        headerItemCount = 0

        if numberColumn == True:
            Label(self, text=self.NUMBER, **headerStyling,
                  ).grid(row=0, column=headerItemCount, sticky=self.GRID_STICKY)
            headerItemCount += 1

        for header in headerList:
            Label(self, text=header.strip().capitalize(
            ), **headerStyling).grid(row=0, column=headerItemCount, sticky=self.GRID_STICKY)
            headerItemCount += 1

        return headerItemCount

    def _createEntries(self, data: list[dict[str, str]], labelCount: int = 0, backgroundOnEven: bool = False, entryStyling: dict[str, str] = {}) -> int:
        for entry in data:
            labelIndex = 0
            background = self.GRID_BACKGROUND if (
                backgroundOnEven and labelCount % 2 == 0) else self.cget(self.BG)
            Label(self, text=labelCount, background=background, **entryStyling).grid(
                row=labelCount, column=labelIndex, sticky=self.GRID_STICKY)
            labelIndex += 1
            for values in entry.values():
                Label(self, text=str(values).strip(), background=background, **entryStyling).grid(
                    row=labelCount, column=labelIndex, sticky=self.GRID_STICKY)
                labelIndex += 1
            labelCount = labelCount + 1

        return labelCount

    def _additionalGridProperties(self, row: int, col: int) -> None:
        self.grid_rowconfigure(0, minsize=self.HEADER_SIZE)
        for i in range(1, row):
            self.grid_rowconfigure(i, minsize=self.ENTRY_SIZE)

        for j in range(col):
            self.grid_columnconfigure(j, weight=1)
