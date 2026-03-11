import time

from pygments.lexer import words

import dictionary as d
import richWord as rw
import os


class MultiDictionary:

    def __init__(self):
       self.italian = d.Dictionary()
       self.english = d.Dictionary()
       self.spanish = d.Dictionary()

    def printDic(self, language):
        dictionary = getattr(self, language.lower())
        return dictionary.printAll()


    def searchWord(self, words, language):
        dictionary = getattr(self, language.lower())
        file_name = os.path.join("resources", f"{language.capitalize()}.txt")
        dictionary.loadDictionary(file_name)
        result = []
        _start = time.time()
        for w in words:
            rwObj = rw.RichWord(w)
            if w not in dictionary.dict:
                rwObj.corretta = False
                result.append(rwObj.__str__())
        _end = time.time()
        tempo = _end - _start
        return result, tempo



    def searchWordLinear(self, words, language):
        dictionary = getattr(self, language.lower())
        result = []
        _start = time.time()

        for w in words:
            rwObj = rw.RichWord(w)
            trovato = ricercaLineare(dictionary.dict, w)
            if not trovato:
                rwObj.corretta = False
                result.append(rwObj.__str__())
        _end = time.time()
        tempo = _end - _start
        return tempo


    def searchWordDichotomic(self, words, language):
        dictionary = getattr(self, language.lower())
        result = []
        _start = time.time()
        centro = round((len(dictionary.dict)-1)/2)
        for w in words:
            rwObj = rw.RichWord(w)
            if dictionary.dict[centro] == w:
                trovato = True
            if dictionary.dict[centro] < w:
                trovato = ricercaDicotomica(dictionary.dict, w, centro, len(dictionary.dict))
            elif dictionary.dict[centro] > w:
                trovato = ricercaDicotomica(dictionary.dict, w, 0, centro)

            if not trovato:
                rwObj.corretta = False
                result.append(rwObj.__str__())
        _end = time.time()
        tempo = _end - _start
        return tempo


def ricercaLineare(words, w):
    for word in words:
        if word == w:
            return True
    return False

def ricercaDicotomica(words, w, iStart, iEnd):
    for i in range(iStart, iEnd):
        if words[i] == w:
            return True
    return False
