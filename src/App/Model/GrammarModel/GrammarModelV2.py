from .GrammarModel import GrammarModel
from ..DictionaryModel import DictionaryModel
from ..Datatype import Grammar, GrammarV2

class GrammarModelV2(GrammarModel):

    def __init__(self) -> None:
        super().__init__()

    def _generateGrammarData(self, content, dm: DictionaryModel = None) -> Grammar:
        return GrammarV2(content[0], content[1], int(content[2]), content[3])
