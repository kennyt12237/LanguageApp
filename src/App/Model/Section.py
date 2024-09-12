from .Datatype import Word, Grammar

class Section():
    
    def __init__(self, name : str, words : list[Word], grammars : list[Grammar], sentences : dict[str,str]) -> None:
        self.name : str = name
        self.words : list[Word] = words
        self.grammars : list[Grammar] = grammars
        self.sentences : dict[str,str] = sentences
        
    def getName(self) -> str:
        return self.name
    
    def getWords(self) -> list[Word]:
        return self.words
    
    def getGrammars(self) -> list[Grammar]:
        return self.grammars

    def getSentences(self) -> dict[str,str]:
        return self.sentences