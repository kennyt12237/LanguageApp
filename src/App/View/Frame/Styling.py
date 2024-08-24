from tkinter.font import NORMAL, BOLD

WIDTH = "width"
HEIGHT = "height"
BACKGROUND = "background"


class TableStyling():

    def __init__(self) -> None:
        self.headerLabelSettings = dict(
            borderwidth=2, relief="groove", font=("Segoe UI", 16))
        self.labelSettings = dict(borderwidth=2, relief="groove")

    def getHeaderLabelSettings(self) -> dict:
        return self.headerLabelSettings

    def getLabelSettings(self) -> dict:
        return self.labelSettings


tableStyling = TableStyling()


def getTableHeaderLabelSettings() -> dict:
    return tableStyling.getHeaderLabelSettings()


def getTableLabelSettings() -> dict:
    return tableStyling.getLabelSettings()


class SentenceStyling():

    def __init__(self) -> None:
        self.sentenceTextFont = ("Segoe UI", 20)
        self.sentenceMeaningFont = ("Segoe UI", 24)
        self.stepLabelFont = ("Couroer", 10, BOLD)

    def setSentenceTextFont(self, font: tuple[str, int]) -> None:
        self.sentenceTextFont = font

    def setSentenceMeaningFont(self, font: tuple[str, int]) -> None:
        self.sentenceMeaningFont = font

    def getSentenceTextFont(self) -> tuple:
        return self.sentenceTextFont

    def getSentenceMeaningFont(self) -> tuple:
        return self.sentenceMeaningFont

    def getStepLabelFont(self) -> tuple:
        return self.stepLabelFont


sentenceStyling = SentenceStyling()


def getSentenceTextFont() -> tuple:
    return sentenceStyling.getSentenceTextFont()


def getSentenceMeaningFont() -> tuple:
    return sentenceStyling.getSentenceMeaningFont()


def getStepLabelFont() -> tuple:
    return sentenceStyling.getStepLabelFont()
