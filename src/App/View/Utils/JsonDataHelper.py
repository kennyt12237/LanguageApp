import json

def getGrammarCharactersList(grammarDataJson: json) -> list[str]:
    grammarData: list[dict[str, str]] = json.loads(grammarDataJson)
    grammars: list[str] = []
    for g in grammarData:
        grammars.append(g["character"])
    return grammars

def getGrammarDataFromCharacter(grammarDataJson : json, character : str) -> dict[str,str]:
    grammarData = json.loads(grammarDataJson)
    for data in grammarData:
        if data["character"] == character:
            return data
    return None