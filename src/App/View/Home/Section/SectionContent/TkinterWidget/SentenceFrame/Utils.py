from enum import Enum
import json


class TkManager(Enum):
    PACK = "Pack"
    GRID = "Grid"
    PLACE = "Place"


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

def getDictionaryCharactersList(dictionaryDataJson: json) -> list[str]:
    dictionaryData : list[dict[str,str]] = json.loads(dictionaryDataJson)
    words : list[str] = []
    for d in dictionaryData:
        words.append(d['character'])
    return words

def getDictionaryDataFromCharacter(dictionaryDataJson: json, character: str) -> dict[str, str]:
    dictionaryData = json.loads(dictionaryDataJson)
    for data in dictionaryData:
        if data["character"] == character:
            return data
    return None
    