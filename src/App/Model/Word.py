from __future__ import annotations
from enum import Enum

class WordType(Enum):
    NOUN  = "noun"
    ADJECTIVE = "adjective"
    VERB = "verb"
    ADVERB = "adverb"
    
WordTypeMap = {
    'noun' : WordType.NOUN,
    'adjective' : WordType.ADJECTIVE,
    'verb' : WordType.VERB,
    'adverb' : WordType.ADVERB
}

class Grammar():
    
    def __init__(self, word : Word, number : int, usage : str) -> None:
        self.word : Word = word
        self.number : int = number
        self.usage : str = usage
    
    def getGrammarWord(self) -> Word:
        return self.word
    
    def getGrammarNumber(self) -> int:
        return self.number
    
    def getUsage(self) -> str:
        return self.usage
    
class Word():
    
    def __init__(self, character : str, pinyin : str, type : WordType, meaning : str) -> None:
        self.character : str = character
        self.pinyin : str = pinyin
        self.type : WordType = type
        self.meaning : str = meaning
        self.grammars : list[Grammar] = []
        
    def getCharacter(self) -> str:
        return self.character
    
    def getPinyin(self) -> str:
        return self.pinyin
    
    def getWordMeaning(self) -> str:
        return self.meaning
    
    def getWordType(self) -> WordType:
        return self.type
    
    def getWordTypeValue(self) -> str:
        return self.type.value
    
    def getAllGrammars(self) -> list[Grammar]:
        return self.grammars
    
    def addGrammar(self, grammar : Grammar) -> None:
        self.grammars.append(grammar)
    
    def __str__(self) -> str:
        return "{character},{pinyin},{wordType},{meaning}".format(
            character=self.getCharacter(),
            pinyin=self.getPinyin(),
            wordType=self.getWordType().value,
            meaning=self.getWordMeaning()
        )