import time

import multiDictionary as md
from dictionary import Dictionary


class SpellChecker:

    def __init__(self):
        self.diz = Dictionary()

    def handleSentence(self, txtIn, language):
        self.diz.loadDictionary(language)
        text = replaceChars(txtIn)
        print(text)
        print(self.diz.printAll())

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
    chars = "\\\"`*_{}[]()>&/?#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
