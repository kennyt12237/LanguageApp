from .Word import Word
from .Section import Section
from .DictionaryModel import DictionaryModel
from .GrammarModel import GrammarModel, GrammarModelV1
from .SectionModel import SectionModel, SectionModelV1


class ChineseLanguageModel:

    def __init__(self, dictionaryModel: DictionaryModel = None, grammarModel: GrammarModel = None, sectionModel: SectionModel = None):
        self.dictionaryModel = dictionaryModel if dictionaryModel != None else DictionaryModel()
        self.grammarModel = grammarModel if grammarModel != None else GrammarModelV1()
        self.sectionModel = sectionModel if sectionModel != None else SectionModelV1()

    def loadDictionaryDataFromTSV(self, filePath: str) -> None:
        self.dictionaryModel.loadDataFromCSVFile(filePath)

    def loadSectionsFolderFromTSV(self, sectionsPath: str) -> None:
        self.sectionModel.loadSectionsDirectory(
            sectionsPath, self.dictionaryModel, self.grammarModel)

    def loadGrammarDataFromTSV(self, filePath: str) -> None:
        self.grammarModel.loadDataFromCSVFile(filePath, self.dictionaryModel)

    def getAllDictionaryWords(self) -> list[Word]:
        return self.dictionaryModel.getAllWords()

    def getAllSections(self) -> list[Section]:
        return self.sectionModel.getAllSections()
