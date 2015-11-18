#	"Poems From Atrus" (#PoemsFromAtrus, @PoemsFromAtrus, https://github.com/hgamiel/PoemsFromAtrus)
#	By Hannah Gamiel (@repolevedemag, @hannahgamiel, hannahgamiel.com, https://github.com/hgamiel)
# 	Uses TwitterAPI for Python (https://github.com/geduldig/TwitterAPI)
#	10/18/2015

from VerseFormatter import *
from FileIO import *
from SentenceGenerator import *

class VerseGenerator:
	_thisVerseFormatter = VerseFormatter()
	_thisSentenceGenerator = SentenceGenerator()
	_maxNumSentences  = 5
	_thisFileIO = FileIO()

	def __init__ (self, mns=5):
		self._maxNumSentences = mns

	def generateVerses(self):
		for _ in range (0, self._maxNumSentences+1):
			s = self._thisSentenceGenerator.getSentenceForVerse()
			fs = self._thisVerseFormatter.getFormattedVerse(s, self._thisFileIO.oBuffer)
			if(fs != ''):
				self._thisFileIO.addToBuffer(fs)
			else:
				break

	def getFileIO(self):
		return self._thisFileIO

	def getVerseFormatter(self):
		return self._thisVerseFormatter
