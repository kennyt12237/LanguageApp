from tkinter.font import Font

from enum import Enum
import json


class TkManager(Enum):
    PACK = "Pack"
    GRID = "Grid"
    PLACE = "Place"


def convertTupleToFont(fontTuple: tuple) -> Font:
    family, size = fontTuple
    return Font(family=family, size=size)


def getGrammarCharactersList(grammarDataJson: json) -> list[str]:
    grammarData: list[dict[str, str]] = json.loads(grammarDataJson)
    grammars: list[str] = []
    for g in grammarData:
        grammars.append(g["character"])
    return grammars


def getGrammarDataFromCharacter(grammarDataJson: json, character: str) -> dict[str, str]:
    grammarData = json.loads(grammarDataJson)
    for data in grammarData:
        if data["character"] == character:
            return data
    return None
