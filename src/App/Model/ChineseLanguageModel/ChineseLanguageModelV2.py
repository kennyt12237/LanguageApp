from .ChineseLanguageModel import ChineseLanguageModel
from ..DictionaryModel import DictionaryModel
from ..GrammarModel import GrammarModel, GrammarModelV2
from ..SectionModel import SectionModel, SectionModelV2

class ChineseLanguageModelV2(ChineseLanguageModel):

    def __init__(self, dictionaryModel: DictionaryModel = None, grammarModel: GrammarModel = None, sectionModel: SectionModel = None):
        super().__init__(dictionaryModel=dictionaryModel, grammarModel=GrammarModelV2(), sectionModel=SectionModelV2())

    def loadSectionsFolderFromTSV(self, sectionsPath: str) -> None:
        self.sectionModel.loadSectionsDirectory(
            sectionsPath, self.dictionaryModel, self.grammarModel)
        self.dictionaryModel.setWords(
            self.sectionModel.getAllWordsFromSections())
        self.grammarModel.setGrammars(
            self.sectionModel.getAllGrammarsFromSection())
