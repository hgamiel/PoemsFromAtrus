#	"Poems From Atrus" (#PoemsFromAtrus, @PoemsFromAtrus, https://github.com/hgamiel/PoemsFromAtrus)
#	By Hannah Gamiel (@repolevedemag, @hannahgamiel, hannahgamiel.com, https://github.com/hgamiel)
# 	Uses TwitterAPI for Python (https://github.com/geduldig/TwitterAPI)
#	10/18/2015

class FileIO:
	_n_read_file = "../textfiles/atrus.txt"
	_n_write_file = "../textfiles/output.txt"
	_open_read_file = open(_n_read_file, 'r')
	_open_write_file = open(_n_write_file, 'w')
	oBuffer = []
	_oString = ''

	def __init__(self, nr="../textfiles/atrus.txt", nw="../textfiles/output.txt"):
		self.__setupFiles(nr, nw)

	def __setupFiles(self, nr, nw):
		if(self._n_read_file != ''):
			self._n_read_file = nr
			self.__applyReadFile()
		if(self._n_write_file != ''):
			self._n_write_file = nw
			self.__applyWriteFile()

	def renameFiles(self, nr, nw):
		self.__setupFiles(nr, nw)

	def __applyReadFile(self):
		self._open_read_file = open(self._n_read_file, 'r')

	def __applyWriteFile(self):
		self._open_write_file = open(self._n_write_file, 'w')	

	def getRawContents(self):
		return self._open_read_file.read()

	def getContentsByLine(self):
		return list(self.getRawContents().split('\n'))

	def addToBuffer(self, addition):
		self.oBuffer.append(addition)

	def __prepareOutput(self, sig):
		self._oString = "\"" + "\n".join(self.oBuffer).strip(' ') + "\"" + "\n" + sig

	def printOutput(self):
		print(self._oString)

	def getOutputString(self):
		return self._oString

	def writeToFile(self, sig):
		self.__prepareOutput(sig)
		self._open_write_file.write(self._oString)

	def __closeFile(self, f):
		f.close()

	def closeFiles(self):
		if(self._open_write_file):
			self.__closeFile(self._open_write_file)
		if(self._open_read_file):
			self.__closeFile(self._open_read_file)

	def finishedGeneration(self, sig):
		self.writeToFile(sig)
		self.printOutput()

		