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
            sectionList.append(self._loadSection(
                os.path.join(sectionsPath, section), dm, gm))
        self.sections = sectionList

    def _loadSection(self, sectionPath: str, dm: DictionaryModel, gm: GrammarModel) -> Section:
        fileToMethod = {
            'words.tsv': self._loadWords,
            'grammars.tsv': self._loadGrammars,
            'sentences.tsv': self._loadSentences,
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

    @abstractmethod
    def _loadWords(self, filePath, dm: DictionaryModel, gm: GrammarModel) -> list[Word]:
        pass

    @abstractmethod
    def _loadGrammars(self, filePath: str, dm: DictionaryModel, gm: GrammarModel) -> list[Grammar]:
        pass

    @abstractmethod
    def _loadSentences(self, filePath: str, dm: DictionaryModel, gm: GrammarModel) -> dict[str, str]:
        pass

    def getAllSections(self) -> list[Section]:
        return self.sections


class SectionModelV1(SectionModel):

    def __init__(self, sections: list[Section] = []) -> None:
        super().__init__(sections)

    def loadSectionsDirectory(self, sectionsPath: str, dm: DictionaryModel = None, gm: GrammarModel = None) -> None:
        sectionList: list[Section] = []
        for section in os.listdir(sectionsPath):
            sectionList.append(self._loadSection(
                os.path.join(sectionsPath, section), dm, gm))
        self.sections = sectionList

    def _loadWords(self, filePath, dm: DictionaryModel, gm: GrammarModel) -> list[Word]:
        wordList: list[Word] = []
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            word = dm.findWordByCharacterAndPinyin(content[0], content[1])
            wordList.append(word)
        return wordList

    def _loadGrammars(self, filePath: str, dm: DictionaryModel, gm: GrammarModel) -> list[Grammar]:
        grammarList: list[Grammar] = []
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            g = gm.findGrammarByCharacterAndNumber(content[0], int(content[1]))
            if g:
                grammarList.append(g)
        return grammarList

    def _loadSentences(self, filePath: str, dm: DictionaryModel, gm: GrammarModel) -> dict[str, str]:
        sentences: dict[str, str] = {}
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            sentences[content[0]] = content[1]
        return sentences