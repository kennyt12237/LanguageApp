from tkinter.font import NORMAL 

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
    
class DictionaryStyling():
    
    def __init__(self) -> None:
        self.headerLabelSettings = dict(borderwidth=2, relief="groove", font=("Segoe UI", 16))
        self.labelSettings = dict(borderwidth=2, relief="groove")
        
    def getHeaderLabelSettings(self) -> dict:
        return self.headerLabelSettings
    
    def getLabelSettings(self) -> dict:
        return self.labelSettings
    
frameStyling = FrameStyling()

def setGridSettings(windowWidth : int, windowHeight : int, relativeSize : float) -> dict[str,str]:
    frameStyling.setGridSettings(windowWidth, windowHeight, relativeSize)
    return frameStyling.getGridSettings()

def getGridSettings() -> dict[str,str]:
    return frameStyling.getGridSettings()

dictionaryStyling = DictionaryStyling()

def getDictionaryHeaderLabelSettings() -> dict:
    return dictionaryStyling.getHeaderLabelSettings()

def getDictionaryLabelSettings() -> dict:
    return dictionaryStyling.getLabelSettings()