from .Section import Section
from .Word import Word, Grammar
from .DictionaryModel import DictionaryModel
from .GrammarModel import GrammarModel

from abc import ABC, abstractmethod
import os


class SectionModel(ABC):

    def __init__(self, sections: list[Section] = []) -> None:
        self.sections: list[Section] = sections

    def loadSectionsDirectory(self, sectionsPath: str, dm: DictionaryModel = None, gm: GrammarModel = None) -> None:
        sectionList: list[Section] = []
        for section in os.listdir(sectionsPath):
            sectionList.append(self.__loadSection(
                os.path.join(sectionsPath, section), dm, gm))
        self.sections = sectionList

    def __loadSection(self, sectionPath: str, dm: DictionaryModel, gm: GrammarModel) -> Section:
        fileToMethod = {
            'words.tsv': self.__loadWords,
            'grammars.tsv': self.__loadGrammars,
            'sentences.tsv': self.__loadSentences,
        }

        fileToVariable = {
            'words.tsv': [],
            'grammars.tsv': [],
            'sentences.tsv': {}
        }
        for file in os.listdir(sectionPath):
            filename = str(file).lower()
            method = fileToMethod[filename]
            res = method(os.path.join(sectionPath, file), dm, gm)
            fileToVariable[filename] = res
        files = list(fileToVariable.keys())
        newWords = fileToVariable[files[0]]
        newGrammar = fileToVariable[files[1]]
        newSentences = fileToVariable[files[2]]
        return Section(sectionPath[sectionPath.rfind("\\")+1:], newWords, newGrammar, newSentences)

    def __loadWords(self, filePath, dm: DictionaryModel = None, gm: GrammarModel = None) -> list[Word]:
        wordList: list[Word] = []
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            word = self._createWord(content, dm, gm)
            wordList.append(word)
        return wordList

    def __loadGrammars(self, filePath: str, dm: DictionaryModel = None, gm: GrammarModel = None) -> list[Grammar]:
        grammarList: list[Grammar] = []
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            g = self._createGrammar(content, dm, gm)
            if g:
                grammarList.append(g)
        return grammarList

    def __loadSentences(self, filePath: str, dm: DictionaryModel = None, gm: GrammarModel = None) -> dict[str, str]:
        sentences: dict[str, str] = {}
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            key, value = self._createSentence(content, dm, gm)
            sentences[key] = value
        return sentences

    @abstractmethod
    def _createWord(self, content, dm: DictionaryModel = None, gm: GrammarModel = None) -> Word:
        pass

    @abstractmethod
    def _createGrammar(self, content, dm: DictionaryModel = None, gm: GrammarModel = None) -> Grammar:
        pass

    @abstractmethod
    def _createSentence(self, content, dm: DictionaryModel = None, gm: GrammarModel = None) -> tuple:
        pass

    def getAllSections(self) -> list[Section]:
        return self.sections


class SectionModelV1(SectionModel):

    def __init__(self, sections: list[Section] = []) -> None:
        super().__init__(sections)

    def _createWord(self, content, dm: DictionaryModel = None, gm: GrammarModel = None) -> Word:
        return dm.findWordByCharacterAndPinyin(content[0], content[1])

    def _createGrammar(self, content, dm: DictionaryModel = None, gm: GrammarModel = None) -> Grammar:
        return gm.findGrammarByCharacterAndNumber(content[0], int(content[1]))

    def _createSentence(self, content, dm: DictionaryModel = None, gm: GrammarModel = None) -> tuple:
        return (content[0], content[1])
