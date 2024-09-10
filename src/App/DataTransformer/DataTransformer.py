from ..Model import Word, Grammar, Section
import json

class DataTransformer():
    
    def wordListToJson(self, words : list[Word]) -> json:
        wordList : list[dict[str,str]] = []
        for word in words:
            wordItem = {}
            wordItem["character"] = word.getCharacter()
            wordItem["pinyin"] = word.getPinyin()
            wordItem["type"] = word.getWordTypeValue()
            wordItem["meaning"] = word.getWordMeaning()
            wordList.append(wordItem)
        return json.dumps(wordList)
    
    def grammarListToJson(self, grammars : list[Grammar]) -> json:
        grammarList : list[dict[str,str]] = []
        for g in grammars:
            grammarItem = {}
            grammarItem["character"] = g.getCharacter()
            grammarItem["pinyin"] = g.getPinyin()
            grammarItem["number"] = g.getGrammarNumber()
            grammarItem["usage"] = g.getUsage()
            grammarList.append(grammarItem)
        return json.dumps(grammarList)
    
    def sentencesToJson(self, sentences : dict[str,str]) -> json:
        sentenceList : list[dict[str,str]] = []
        for key in sentences.keys():
            sentenceItem = {}
            sentenceItem["sentence"] = key
            sentenceItem["meaning"] = sentences[key]
            sentenceList.append(sentenceItem)
        return json.dumps(sentenceList)
    
    def sectionListToJson(self, sections : list[Section]) -> json:
        sectionList = {}
        for section in sections:
            sectionItem = {}
            sectionItem["words"] = self.wordListToJson(section.getWords()) 
            sectionItem["grammars"] = self.grammarListToJson(section.getGrammars())
            sectionItem["sentences"] = self.sentencesToJson(section.getSentences())
            sectionList[section.getName()] = sectionItem
        return json.dumps(sectionList)