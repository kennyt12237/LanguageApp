import ctypes

def setProcessDpiAwareness2() -> None:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    
def getScreenWidthCtypes() -> tuple:
    return ctypes.windll.user32.GetSystemMetrics(0)

def getScreenHeightCtypes() -> tuple:
    return ctypes.windll.user32.GetSystemMetrics(1)