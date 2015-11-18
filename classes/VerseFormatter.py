#	"Poems From Atrus" (#PoemsFromAtrus, @PoemsFromAtrus, https://github.com/hgamiel/PoemsFromAtrus)
#	By Hannah Gamiel (@repolevedemag, @hannahgamiel, hannahgamiel.com, https://github.com/hgamiel)
# 	Uses TwitterAPI for Python (https://github.com/geduldig/TwitterAPI)
#	10/18/2015

import math
import random

class VerseFormatter:
	_sig = ''
	_clim = 140
	_minwps = 3 # minimum words per sentence
	_minwpl = 5 # minimum words per line with >= 8 words
	_maxwpl = 8 # maximum words per line with >= 8 words
	_uclim = 1 # whether or not to character limit
	_fclim = 0 # final character limit (calculated in constructor)
	_rccnt = 0
	_fcnt = 0 # final character count
	_surroundWithQuotes = 1
	_newLineAfterPoem = 1
	_extraCharsNum = 0

	def __init__(self, s='#PoemsFromAtrus', c=140, mwps = 3, miwpl = 5, mawpl = 8, ucl = 1, swq = 1, nlap = 1):
		self._sig = s
		self._clim = c
		self._minwps = mwps
		self._minwpl = miwpl
		self._maxwpl = mawpl
		self._uclim = ucl
		self._surroundWithQuotes = swq
		self._newLineAfterPoem = nlap
		self.__setExtraCharsNum()
		self._fclim = self._clim - len(self._sig) - self._extraCharsNum # tweet character limit considering the signature and two quotation marks

	def __getMaxNumLinesPossible(self, s):
		return (math.ceil(len(s) / self._minwpl) if (len(s) > self._minwpl) else 1) # get max num of lines possible

	def __setExtraCharsNum(self):
		extraChars = 0
		if(self._surroundWithQuotes):
			self._extraCharsNum += 1
		if(self._newLineAfterPoem):
			self._extraCharsNum += 1

	def __checkMaxNumCharsPossible(self, s, buff):
		checkmax = (self._rccnt + self._extraCharsNum + len(' '.join(s).strip(' ')) + self.__getMaxNumLinesPossible(s) + len(buff)) # check the current max (+ possible upper limit) num of characters at the moment
		return (not self._uclim or (self._uclim and checkmax < self._fclim))

	def __checkNumWordsAgainstMax(self, s):
		return (len(s) > self._maxwpl)

	def __getRandomIndexWithinBounds(self, s):
		return random.randint(self._minwpl, self._maxwpl)

	def __separateSentence(self, s):
		finalList = []
		low = 0
		top = self.__getRandomIndexWithinBounds(s)
		while(low < len(s)):
			tempstr = ''
			for i in range(low, top):
				tempstr += s[i] + ' '
			low = top
			newrand = self.__getRandomIndexWithinBounds(s)
			top = top + newrand if (top + newrand < len(s)) else len(s)
			finalList.append(tempstr.strip(' '))
		return '\n'.join(finalList)

	def getFormattedVerse(self, s, buff):
		fv = ''
		if(self.__checkMaxNumCharsPossible(s, buff)):
			if(len(s) > self._maxwpl):
				fv = self.__separateSentence(s)
			else:
				fv = ' '.join(s).strip()
			self._rccnt += len(fv)
		elif(self._uclim and len(buff) == 0):
			self._rccnt = 0
		elif(self._uclim):
			self._fcnt = len("\"" + "\n".join(buff) + "\"" + "\n" + self._sig) # final char count
			print("Breaking: Character count = " + str(self._fcnt) + "\n")
			return ''
		return fv

	def getSig(self):
		return self._sig
