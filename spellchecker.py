import string
import time
import multiDictionary as md
from multiDictionary import MultiDictionary


class SpellChecker:

    def __init__(self):
        self.md = MultiDictionary()

    def handleSentence(self, txtIn, language):
        text = replaceChars(txtIn.lower().strip())
        words = text.split()
        result, tempo = self.md.searchWord(words, language)

        print(f"Errori trovati: {len(result)}\n")
        for w in result:
            print(f"{w}\n")
        print(f"Time using in/not in: {tempo}")


        tempo = self.md.searchWordLinear(words, language)
        print(f"Time using linear search: {tempo}")

        tempo = self.md.searchWordDichotomic(words, language)
        print(f"Time using dichotomic search: {tempo}")



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    for char in text:
        if char in string.punctuation:
            text = text.replace(char, "")
    return text