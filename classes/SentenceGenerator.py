#	"Poems From Atrus" (#PoemsFromAtrus, @PoemsFromAtrus, https://github.com/hgamiel/PoemsFromAtrus)
#	By Hannah Gamiel (@repolevedemag, @hannahgamiel, hannahgamiel.com, https://github.com/hgamiel)
# 	Uses TwitterAPI for Python (https://github.com/geduldig/TwitterAPI)
#	10/18/2015

from RuleSet import *
from FileIO import *
import re
import random

class SentenceGenerator:
	_thisFileIO = FileIO()
	_thisRuleSet = RuleSet()
	_lc = 1
	_li = 0
	_sentences = []
	_minwps = -1
	_rm = 1

	def __init__ (self, mwps=2, randMod=1):
		self.__grabSentencesFromFile()
		self._minwps = mwps
		self._rm = randMod

	def __grabSentencesFromFile(self):
		self._sentences = list(re.split(r' *[\.\?!][\'"\)\]]* *', self._thisFileIO.getRawContents())) # list of sentences

	def __getRandomSentenceFromFeed(self):
		s = []
		ni = random.randint(0, len(self._sentences)-1) # new index
		if(self._rm):
			while((ni == self._li) or (ni + 1 == self._li) or (ni - 1 == self._li)):
				ni = random.randint(0, len(self._sentences)-1)
			self._li = ni
			s = list(self._sentences[self._li].split(' '))
		else:
			s = list(random.choice(self._sentences).split(' '))
		return s

	def __getLastWordWithPunc(self, s):
		p = self._thisRuleSet.getRandomPunc()
		return str(s[len(s)-1]+p)

	def __putPuncOnLastWord(self, s, lw):
		s[len(s)-1] = ''.join(lw)
		return s

	def __getPreparedSentence(self):
		s = self.__getRandomSentenceFromFeed()
		lw = self.__getLastWordWithPunc(s)
		s = self.__putPuncOnLastWord(s, lw)
		s[0] = self.__modifyFirstChar(s)
		self.__setLastCapGlobal(s)
		return s

	def __setLastCapGlobal(self, s): # set the global cap bool for use in next sentence creation
		lastchar = s[len(s)-1][-1::]
		if (self._thisRuleSet.isWordProperNoun(lastchar)):
			self._lc = 1
		else:
			self._lc = 0

	def __modifyFirstChar(self, s): # figure out whether or not to capitalize the first letter of a sentence
		ffw = ''; # final first word
		ofw = s[0] # original first word of sentence
		ofl = ofw[0] # original first letter of sentence
		iofw =  ofw[1:len(s[0])] # original first word minus first letter

		if (self._lc == 1 or self._thisRuleSet.isWordProperNoun(ofw.lower())):
			ffw = ''.join(ofl.upper() + iofw)
		else:
			ffw = ''.join(ofl.lower() + iofw)
		return ffw

	def getSentenceForVerse(self):
		ns = self.__getPreparedSentence()
		while(len(ns) < self._minwps and self._minwps >= 0):
			ns = self.__getPreparedSentence()
		return ns