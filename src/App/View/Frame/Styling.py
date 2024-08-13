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
    
frameStyling = FrameStyling()

def setGridSettings(windowWidth : int, windowHeight : int, relativeSize : float) -> dict[str,str]:
    frameStyling.setGridSettings(windowWidth, windowHeight, relativeSize)
    return frameStyling.getGridSettings()

def getGridSettings() -> dict[str,str]:
    return frameStyling.getGridSettings()