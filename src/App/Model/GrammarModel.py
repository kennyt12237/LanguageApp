from .Word import Word, Grammar, GrammarV1
from .DictionaryModel import DictionaryModel

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

    def addGrammar(self, grammar: Grammar) -> None:
        self.grammars.append(grammar)

    def removeGrammar(self, grammar: Grammar) -> None:
        self.grammars.remove(grammar)

    def getAllGrammar(self) -> list[Grammar]:
        return self.grammars


class GrammarModelV1(GrammarModel):

    def __init__(self) -> None:
        super().__init__()

    def _generateGrammarData(self, content, dm: DictionaryModel = None) -> Grammar:
        word = dm.findWordByCharacterAndPinyin(content[0], content[1])
        newGrammar = GrammarV1(word.getCharacter(), word.getPinyin(), int(
            content[2]), content[3], word)
        word.addGrammar(newGrammar)
        return newGrammar

class GrammarModelV2(GrammarModel):

    def __init__(self) -> None:
        super().__init__()

    def _generateGrammarData(self, content, dm: DictionaryModel = None) -> Grammar:
        return Grammar(content[0], content[1], int(content[2]), content[3])
