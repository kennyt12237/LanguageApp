from tkinter.font import NORMAL, BOLD


class SentenceStyling():

    def __init__(self) -> None:
        self.sentenceTextFont = ("Segoe UI", 20)
        self.sentenceMeaningFont = ("Segoe UI", 24)
        self.stepLabelFont = ("MS Sans Serif", 10, BOLD)

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
