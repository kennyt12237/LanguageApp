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
    
    def loadDictionaryDataFromTSV(self, filePath : str) -> None:
        self.dictionaryModel.loadDataFromCSVFile(filePath)
    
    def loadSectionsFolderFromTSV(self, sectionsPath : str) -> None:
        self.sectionModel.loadSectionsDirectory(sectionsPath, self.dictionaryModel, self.grammarModel)
        
    def loadGrammarDataFromTSV(self, filePath : str) -> None:
        self.grammarModel.loadDataFromCSVFile(filePath, self.dictionaryModel)
        
    def loadAllFromSectionFolderTSV(self, filePath : str) -> None:
        wl, gl, _ = self.sectionModel.loadSectionsDirectory1(filePath)
        self.dictionaryModel.setWordList(wl)
        self.grammarModel.setGrammarList(gl)
        
    def getAllDictionaryWords(self) -> list[Word]:
        return self.dictionaryModel.getAllWords()
    
    def getAllSections(self) -> list[Section]:
        return self.sectionModel.getAllSections()