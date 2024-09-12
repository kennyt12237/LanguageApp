from .SectionModel import *
from ..Section import Section

class SectionModelV1(SectionModel):

    def __init__(self, sections: list[Section] = []) -> None:
        super().__init__(sections)

    def _createWord(self, content, dm: DictionaryModel = None, gm: GrammarModel = None) -> Word:
        return dm.findWordByCharacterAndPinyin(content[0], content[1])

    def _createGrammar(self, content, dm: DictionaryModel = None, gm: GrammarModel = None) -> Grammar:
        return gm.findGrammarByCharacterAndNumber(content[0], int(content[1]))

    def _createSentence(self, content, dm: DictionaryModel = None, gm: GrammarModel = None) -> tuple:
        return (content[0], content[1])

