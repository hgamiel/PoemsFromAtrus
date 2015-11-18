#	"Poems From Atrus" (#PoemsFromAtrus, @PoemsFromAtrus, https://github.com/hgamiel/PoemsFromAtrus)
#	By Hannah Gamiel (@repolevedemag, @hannahgamiel, hannahgamiel.com, https://github.com/hgamiel)
# 	Uses TwitterAPI for Python (https://github.com/geduldig/TwitterAPI)
#	10/18/2015

from TwitterAPI import TwitterAPI
from APIInformation import *
from FileIO import *

class APIHandler:
	_thisFileIO = FileIO("../textfiles/creds.txt")
	_thisAPIInformation = APIInformation() 
	_api = ''

	def __init__(self):
		self.__setInformation()
		self.__connectAPI()

	def __setInformation(self):
		self._thisAPIInformation.setCredsFromLines(self._thisFileIO.getContentsByLine())

	def __connectAPI(self): # connect to Twitter's API
		creds = self._thisAPIInformation.getCredsArray()
		try:
			self._api = TwitterAPI(creds[0], creds[1], creds[2], creds[3])
		except:
			print("Unable to connect to TwitterAPI.\n")

	def tweet(self, s):
		print("\nTweeting...")
		req = self._api.request('statuses/update', {'status': s})
		print('Tweet successful!' if req.status_code == 200 else 'Tweet unsuccessful.')