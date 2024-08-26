
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