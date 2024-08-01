from ..Model import ChineseLanguageModel
from ..View import BasicView
from ..DataTransformer import DataTransformer
import json
class Controller():
    
    def __init__(self, model : ChineseLanguageModel , view : BasicView, dataTransformer : DataTransformer) -> None:
        self.model = model
        self.view = view
        self.dataTransformer = dataTransformer
        
    def start(self) -> None:
        self._loadModels("src\ChineseWordList.csv","src\ChineseGrammarList.csv", "src\sections")
        self._attachListeners()
        self.view.mainloop()
        
    def _loadModels(self, wordPath : str, grammarPath : str, sectionPath : str) -> None:
        self.model.loadDictionaryDataFromCSV(wordPath)
        self.model.loadGrammarDataFromCSV(grammarPath)
        self.model.loadSectionsFolderFromCSV(sectionPath)
        
    def _attachListeners(self) -> None:
        self.view.attachToDictionaryButton(self.requestDictionaryData)
        self.view.attachToSectionButton(self.requestSectionData)
    
    def requestDictionaryData(self) -> json:
        return self.dataTransformer.wordListToJson(self.model.getAllDictionaryWords())
    
    def requestSectionData(self) -> json:
        return self.dataTransformer.sectionListToJson(self.model.getAllSections())