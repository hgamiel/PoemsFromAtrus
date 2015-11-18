#	"Poems From Atrus" (#PoemsFromAtrus, @PoemsFromAtrus, https://github.com/hgamiel/PoemsFromAtrus)
#	By Hannah Gamiel (@repolevedemag, @hannahgamiel, hannahgamiel.com, https://github.com/hgamiel)
# 	Uses TwitterAPI for Python (https://github.com/geduldig/TwitterAPI)
#	10/18/2015

import random

class RuleSet:
	_punc = []
	_puncRequireCap = []
	_pNouns = []

	def __init__(self):
		self._punc = ["?", "--", ".", ",", "!", " ", ";", ".", " ", "..."] # list of puncation
		self._puncRequireCap = ["?", ".", "!", ":", ";"] # list of punctuation that requires capitalized letter after
		self._pNouns = ["catherine", "atrus", "achenar", "sirrus", "d'ni", "i"] # list of names/proper nouns

	def addToPuncList(self, newPunc):
		self._punc.append(newPunc)

	def addToPuncRequireCapList(self, newPRC):
		self._puncRequireCap.append(newPRC)

	def addToProperNounList(self, newPN):
		self._pNouns.append(newPN)

	def getRandomPunc(self):
		return random.choice(self._punc)

	def isWordProperNoun(self, word):
		return (word in self._pNouns)

	def isCharExclamation(self, char):
		return (char in self._puncRequireCap)