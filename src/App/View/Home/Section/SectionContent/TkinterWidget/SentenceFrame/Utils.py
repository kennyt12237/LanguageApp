from enum import Enum
import json


class TkManager(Enum):
    PACK = "Pack"
    GRID = "Grid"
    PLACE = "Place"


def getGrammarCharactersList(grammarData: list[dict[str,str]]) -> list[str]:
    grammars: list[str] = []
    for g in grammarData:
        grammars.append(g["character"])
    return grammars


def getGrammarDataFromCharacter(grammarData: list[dict[str,str]], character: str) -> dict[str, str]:
    for data in grammarData:
        if data["character"] == character:
            return data
    return None

def getDictionaryCharactersList(dictionaryData: list[dict[str,str]]) -> list[str]:
    words : list[str] = []
    for d in dictionaryData:
        words.append(d['character'])
    return words

def getDictionaryDataFromCharacter(dictionaryData: list[dict[str,str]], character: str) -> dict[str, str]:
    for data in dictionaryData:
        if data["character"] == character:
            return data
    return None
    