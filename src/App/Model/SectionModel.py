from .Section import Section
from .Word import Word, Grammar, WordTypeMap
from .DictionaryModel import DictionaryModel
from .GrammarModel import GrammarModel

import os

class SectionModel():
    
    def __init__(self, sections : list[Section] = []) -> None:
        self.sections : list[Section] = sections
        
    def loadSectionsDirectory(self, sectionsPath : str, dm : DictionaryModel, gm : GrammarModel) -> None:
        sectionList : list[Section] = []
        for section in os.listdir(sectionsPath):
            sectionList.append(self._loadSection(os.path.join(sectionsPath,section), dm, gm))
        self.sections = sectionList
    
    def _loadSection(self, sectionPath : str, dm : DictionaryModel, gm : GrammarModel) -> Section:        
        fileToMethod = {
            'words.tsv' : self._loadWords,
            'grammars.tsv' : self._loadGrammars,
            'sentences.tsv' : self._loadSentences,
        }
                
        fileToVariable = {
            'words.tsv' : [],
            'grammars.tsv' : [],
            'sentences.tsv' : {}
        }
        for file in os.listdir(sectionPath):
            filename = str(file).lower()
            method = fileToMethod[filename]
            res = method(os.path.join(sectionPath, file), dm, gm)
            fileToVariable[filename] = res
        files = list(fileToVariable.keys())
        newWords = fileToVariable[files[0]]
        newGrammar = fileToVariable[files[1]]
        newSentences = fileToVariable[files[2]]
        return Section(sectionPath[sectionPath.rfind("\\")+1:], newWords, newGrammar, newSentences)
            
    def _loadWords(self, filePath, dm : DictionaryModel, gm : GrammarModel) -> list[Word]:
        wordList : list[Word] = []
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            word = dm.findWordByCharacterAndPinyin(content[0], content[1])
            wordList.append(word)
        return wordList
        
    def _loadGrammars(self, filePath : str, dm : DictionaryModel, gm : GrammarModel) -> list[Grammar]:
        grammarList : list[Grammar] = []
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            g = gm.findGrammarByCharacterAndNumber(content[0], int(content[1]))
            if g:
                grammarList.append(g)
        return grammarList
    
    def _loadSentences(self, filePath : str, dm : DictionaryModel, gm : GrammarModel) -> dict[str,str]:
        sentences : dict[str,str] = {}
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            sentences[content[0]] = content[1]
        return sentences
    
    def getAllSections(self) -> list[Section]:
        return self.sections

    def loadSectionsDirectory1(self, sectionPath : str) -> tuple:
        sectionList : list[Section] = []
        wordList : list[Word] = []
        grammarList : list[Grammar] = []
        
        for section in os.listdir(sectionPath):
            sec = self._loadSection1(os.path.join(sectionPath, section))
            sectionList.append(sec)
            wordList.extend(sec.getWords())
            grammarList.extend(sec.getGrammars())
        
        self.sections = sectionList
        return (wordList, grammarList, sectionList)
            
    def _loadSection1(self, sectionPath : str) -> Section:
        fileToMethod = {
            'words.tsv' : self._loadWords1,
            'grammars.tsv' : self._loadGrammars1,
            'sentences.tsv' : self._loadSentences1,
        }
                
        fileToVariable = {
            'words.tsv' : [],
            'grammars.tsv' : [],
            'sentences.tsv' : {}
        }
        
        for file in os.listdir(sectionPath):
            filename = str(file).lower()
            method = fileToMethod[filename]
            res = method(os.path.join(sectionPath, file))
            fileToVariable[filename] = res
        files = list(fileToVariable.keys())
        newWords = fileToVariable[files[0]]
        newGrammar = fileToVariable[files[1]]
        newSentences = fileToVariable[files[2]]
        return Section(sectionPath[sectionPath.rfind("\\")+1:], newWords, newGrammar, newSentences)
            
    def _loadWords1(self, filePath) -> list[Word]:
        wordList : list[Word] = []
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            word = Word(content[0], content[1], WordTypeMap.get(content[2].lower()), content[3])
            wordList.append(word)
        return wordList
        
    def _loadGrammars1(self, filePath : str) -> list[Grammar]:
        grammarList : list[Grammar] = []
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            g = Grammar(content[0], content[1], content[2], content[3])
            if g:
                grammarList.append(g)
        return grammarList
    
    def _loadSentences1(self, filePath : str) -> dict[str,str]:
        sentences : dict[str,str] = {}
        file = open(filePath, "r", encoding="utf-8")
        file.readline()
        for line in file:
            content = line.strip().split("\t")
            sentences[content[0]] = content[1]
        return sentences