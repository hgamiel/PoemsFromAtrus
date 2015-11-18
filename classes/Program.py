#	"Poems From Atrus" (#PoemsFromAtrus, @PoemsFromAtrus, https://github.com/hgamiel/PoemsFromAtrus)
#	By Hannah Gamiel (@repolevedemag, @hannahgamiel, hannahgamiel.com, https://github.com/hgamiel)
# 	Uses TwitterAPI for Python (https://github.com/geduldig/TwitterAPI)
#	10/18/2015

from VerseGenerator import *
from APIHandler import *

class Program:

	_thisVerseGenerator = VerseGenerator()
	_thisAPIHandler = APIHandler()

	def __init__(self):
		self._thisVerseGenerator.generateVerses()

	def outputPoem(self):
		self._thisVerseGenerator.getFileIO().finishedGeneration(self._thisVerseGenerator.getVerseFormatter().getSig())
		self._thisAPIHandler.tweet(self._thisVerseGenerator.getFileIO().getOutputString())
		self._thisVerseGenerator.getFileIO().closeFiles()

	def outputFileContents(self):
		self._thisVerseGenerator.getFileIO()

newProgram = Program()
newProgram.outputPoem()