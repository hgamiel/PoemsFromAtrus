#	"Poems From Atrus" (#PoemsFromAtrus, @PoemsFromAtrus, https://github.com/hgamiel/PoemsFromAtrus)
#	By Hannah Gamiel (@repolevedemag, @hannahgamiel, hannahgamiel.com, https://github.com/hgamiel)
# 	Uses TwitterAPI for Python (https://github.com/geduldig/TwitterAPI)
#	10/18/2015

class APIInformation:
	_CONSUMER_KEY = ''
	_CONSUMER_SECRET = ''
	_ACCESS_TOKEN_KEY = ''
	_ACCESS_TOKEN_SECRET = ''

	def __init__ (self, ck='', cs='', atk='', ats=''):
		self.setCredsDirectly(ck, cs, atk, ats)

	def setCredsDirectly(self, ck, cs, atk, ats):
		self._CONSUMER_KEY = ck
		self._CONSUMER_SECRET = cs
		self._ACCESS_TOKEN_KEY = atk
		self._ACCESS_TOKEN_SECRET = ats

	def setCredsFromLines(self, lines):
		self.setCredsDirectly((str(lines[0])), str(lines[1]), str(lines[2]), str(lines[3]))

	def getCredsArray(self):
		return [self._CONSUMER_KEY, self._CONSUMER_SECRET, self._ACCESS_TOKEN_KEY, self._ACCESS_TOKEN_SECRET]