from tkinter.font import NORMAL, BOLD

WIDTH = "width"
HEIGHT = "height"
BACKGROUND = "background"
    
class FrameStyling():
    
    def __init__(self, windowWidth : int = 0, windowHeight : int = 0, relativeSize : float = 0) -> None:
        gridSetting = self.setGridSettings(windowWidth, windowHeight, relativeSize)
    
    def setGridSettings(self, windowWidth : int, windowHeight : int, relativeSize : float) -> None:
        gridSettings : dict[str,str] = {}
        gridSettings[WIDTH] = windowWidth
        gridSettings[HEIGHT] = int(windowHeight * relativeSize)
        gridSettings[BACKGROUND] = "green"
        self.gridSetting = gridSettings

    def getGridSettings(self) -> dict[str,str]:
        return self.gridSetting
    
class TableStyling():
    
    def __init__(self) -> None:
        self.headerLabelSettings = dict(borderwidth=2, relief="groove", font=("Segoe UI", 16))
        self.labelSettings = dict(borderwidth=2, relief="groove")
        
    def getHeaderLabelSettings(self) -> dict:
        return self.headerLabelSettings
    
    def getLabelSettings(self) -> dict:
        return self.labelSettings
    
class SentenceStyling():
    
    def __init__(self) -> None:
        self.sentenceTextFont = ("Segoe UI", 18)
        self.sentenceMeaningFont = ("Segoe UI", 20)
        self.stepLabelFont = ("Couroer", 10, BOLD)
        
    def setSentenceTextFont(self, font : tuple[str, int]) -> None:
        self.sentenceTextFont = font
    
    def setSentenceMeaningFont(self, font : tuple[str, int]) -> None:
        self.sentenceMeaningFont = font
    
    def getSentenceTextFont(self) -> tuple:
        return self.sentenceTextFont
    
    def getSentenceMeaningFont(self) -> tuple:
        return self.sentenceMeaningFont
    
    def getStepLabelFont(self) -> tuple:
        return self.stepLabelFont
    
frameStyling = FrameStyling()

def setGridSettings(windowWidth : int, windowHeight : int, relativeSize : float) -> dict[str,str]:
    frameStyling.setGridSettings(windowWidth, windowHeight, relativeSize)
    return frameStyling.getGridSettings()

def getGridSettings() -> dict[str,str]:
    return frameStyling.getGridSettings()

tableStyling = TableStyling()

def getTableHeaderLabelSettings() -> dict:
    return tableStyling.getHeaderLabelSettings()

def getTableLabelSettings() -> dict:
    return tableStyling.getLabelSettings()

sentenceStyling = SentenceStyling()

def getSentenceTextFont() -> tuple:
    return sentenceStyling.getSentenceTextFont()

def getSentenceMeaningFont() -> tuple:
    return sentenceStyling.getSentenceMeaningFont()

def getStepLabelFont() -> tuple:
    return sentenceStyling.getStepLabelFont()