from ..Datatype import Word, WordTypeMap

class DictionaryModel():
    def __init__(self) -> None:
        self.words : list[Word] = []
    
    def loadDataFromCSVFile(self, filePath : str) -> None:
        file = open(filePath, "r", encoding='utf-8')
        file.readline()
        
        wordList : list[Word] = []
        for line in file:
           word = self._processLineWithData(line)
           wordList.append(word)
        self.words = wordList
        
    def _processLineWithData(self, line : str) -> Word:
        data = line.strip().split("\t")
        character = data[0]
        pinyin = data[1]
        characterType = WordTypeMap.get(data[2].lower())
        meaning = data[3]
        return Word(character, pinyin, characterType, meaning)
        
    def addWord(self, word : Word) -> None:
        self.words.append(word)
        
    def removeWord(self, word : Word) -> None:
        self.words.remove(word)
        
    def getAllWords(self) -> list[Word]:
        return self.words
    
    def setWords(self, words : list[Word]) -> None:
        self.words = words
    
    def findWordByCharacterAndPinyin(self, character : str, pinyin : str) -> Word:
        for word in self.words:
            if word.getCharacter() == character and word.getPinyin() == pinyin:
                return word
        return None