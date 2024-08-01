from .Word import Word
from .Section import Section
from .DictionaryModel import DictionaryModel
from .GrammarModel import GrammarModel
from .SectionModel import SectionModel

class ChineseLanguageModel:
    
    def __init__(self):
        self.dictionaryModel = DictionaryModel()
        self.grammarModel = GrammarModel()
        self.sectionModel = SectionModel()
    
    def loadDictionaryDataFromCSV(self, filePath : str) -> None:
        self.dictionaryModel.loadDataFromCSVFile(filePath)
    
    def loadSectionsFolderFromCSV(self, sectionsPath : str) -> None:
        self.sectionModel.loadSectionsDirectory(sectionsPath, self.dictionaryModel, self.grammarModel)
        
    def loadGrammarDataFromCSV(self, filePath : str) -> None:
        self.grammarModel.loadDataFromCSVFile(filePath, self.dictionaryModel)
        
    def getAllDictionaryWords(self) -> list[Word]:
        return self.dictionaryModel.getAllWords()
    
    def getAllSections(self) -> list[Section]:
        return self.sectionModel.getAllSections()