from .Word import Word, Grammar
from .DictionaryModel import DictionaryModel

class GrammarModel():
    
    def __init__(self) -> None:
        self.grammars : list[Grammar] = []
        
    def loadDataFromCSVFile(self, filePath : str, dm : DictionaryModel) -> None:
        grammarList : list[Grammar] = []
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            word = dm.findWordByCharacterAndPinyin(content[0], content[1])
            newGrammar = Grammar(word,int(content[2]),content[3])
            word.addGrammar(newGrammar)
            grammarList.append(newGrammar)
        self.grammars = grammarList
    
    def findGrammarByCharacterAndNumber(self, character : str, number : int) -> Grammar:
        for g in self.grammars:
            word = g.getGrammarWord()
            if word.getCharacter() == character and g.getGrammarNumber() == number:
                return g
        return None
            
    def setGrammarList(self, grammars : list[Grammar]) -> None:
        self.grammars = grammars
    def addGrammar(self, grammar : Grammar) -> None:
        self.grammars.append(grammar)
        
    def removeGrammar(self, grammar : Grammar) -> None:
        self.grammars.remove(grammar)
        
    def getAllGrammar(self) -> list[Grammar]:
        return self.grammars