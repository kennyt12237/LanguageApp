from .SectionModel import SectionModel
from ..Datatype import Word, Grammar, GrammarV2, WordTypeMap
from ..Section import Section
from ..DictionaryModel import DictionaryModel
from ..GrammarModel import GrammarModel

class SectionModelV2(SectionModel):

    def __init__(self, sections: list[Section] = []) -> None:
        super().__init__(sections)

    def _createWord(self, content, dm: DictionaryModel = None, gm: GrammarModel = None) -> Word:
        return Word(content[0], content[1], WordTypeMap.get(content[2]), content[3])

    def _createGrammar(self, content, dm: DictionaryModel = None, gm: GrammarModel = None) -> Grammar:
        return GrammarV2(content[0], content[1], int(content[2]), content[3])

    def _createSentence(self, content, dm: DictionaryModel = None, gm: GrammarModel = None) -> tuple:
        return (content[0], content[1])
