from .GrammarModel import GrammarModel
from ..DictionaryModel import DictionaryModel
from ..Datatype import Grammar, GrammarV1

class GrammarModelV1(GrammarModel):

    def __init__(self) -> None:
        super().__init__()

    def _generateGrammarData(self, content, dm: DictionaryModel = None) -> Grammar:
        word = dm.findWordByCharacterAndPinyin(content[0], content[1])
        newGrammar = GrammarV1(word.getCharacter(), word.getPinyin(), int(
            content[2]), content[3], word)
        word.addGrammar(newGrammar)
        return newGrammar