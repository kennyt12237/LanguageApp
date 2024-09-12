from ..Datatype import Grammar
from ..DictionaryModel import DictionaryModel

from abc import ABC, abstractmethod


class GrammarModel(ABC):

    def __init__(self) -> None:
        self.grammars: list[Grammar] = []

    def loadDataFromCSVFile(self, filePath: str, dm: DictionaryModel = None) -> None:
        grammarList: list[Grammar] = []
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            grammar = self._generateGrammarData(content, dm)
            grammarList.append(grammar)
        self.grammars = grammarList

    @abstractmethod
    def _generateGrammarData(self, content, dm: DictionaryModel = None) -> Grammar:
        pass

    def findGrammarByCharacterAndNumber(self, character: str, number: int) -> Grammar:
        for g in self.grammars:
            if g.getCharacter() == character and g.getNumber() == number:
                return g
        return None

    def setGrammars(self, grammars : list[Grammar]) -> None:
        self.grammars = grammars
        
    def addGrammar(self, grammar: Grammar) -> None:
        self.grammars.append(grammar)

    def removeGrammar(self, grammar: Grammar) -> None:
        self.grammars.remove(grammar)

    def getAllGrammar(self) -> list[Grammar]:
        return self.grammars
