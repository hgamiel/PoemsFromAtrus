# Atrus script

import re
import random
from random import randint

f_output = open('output.txt','w')
f_feed = open('atrus.txt','r')
r_feed = f_feed.read()

punc = ["?", "--", ".", ",", "!", " ", ";", ".", " "] #list of puncation
puncRequireCap = ["?", ".", "!", ":", ";"] #list of punctuation that requires capitalized letter after
sentences = list(re.split(r' *[\.\?!][\'"\)\]]* *', r_feed)) #list of sentences
pNouns = ["catherine", "atrus", "achenar", "sirrus", "d'ni"] #list of names/proper nouns

oBuffer = []
oString = ""
sig = "\n#PoemsFromAtrus"

n = 5 #num sentences
rm = 1 #random modifier
minwps = 3 #minimum words per sentence
minwpl = 5 #minimum words per line
maxwpl = 8 #maximum words per line
lc = 1 #last cap bool
lastIndex = 0 #last sentence index
clim = 140 - len(sig) #twitter character limit
uclim = 1 #whether or not to character limit

def addToOutput(segment):
	oBuffer.append(segment)

def prepareOutput():
	global oString
	oString = "\"" + "\n".join(oBuffer) + "\"" + "\n" + sig
	f_output.write(oString)

def printOutput():
	print(oString)

def createSentence():
	global lastIndex
	s = []
	newIndex = randint(0, len(sentences)-1)

	if(rm):
		while((newIndex == lastIndex) or (newIndex + 1 == lastIndex) or (newIndex - 1 == lastIndex)):
			newIndex = randint(0, len(sentences)-1)
		lastIndex = newIndex
		s = list(sentences[lastIndex].split(' '))
	else:
		s = list(random.choice(sentences).split(' '))
	p = random.choice(punc)
	lw = str(s[len(s)-1]+p)
	s[len(s)-1] = ''.join(lw)
	return s

def modifyFirstChar(verse):
	ffw = ''; #final first word
	ofw = verse[0] #original first word of verse
	ofl = ofw[0] #original first letter of verse
	iofw =  ofw[1:len(verse[0])] #original first word minus first letter

	if (lc == 1 or (ofl == "i" and len(ofw) == 1) or ofw.lower() in pNouns):
		ffw = ''.join(ofl.upper() + iofw)
	else:
		ffw = ''.join(ofl.lower() + iofw)
	return ffw

def setLastCapGlobal(verse):
	lastchar = verse[len(verse)-1][-1::]

	if (lastchar in puncRequireCap):
		lc = 1
	else:
		lc = 0

def getSentence(mwps):
	s = createSentence()
	while(len(s) < mwps):
		s = createSentence()
	return s

def createVerseFromSentence(sentence):
	verse = sentence
	verse[0] = modifyFirstChar(verse)
	setLastCapGlobal(verse)
	return verse

def getVerses():
	lastRandomNum = 0

	for _ in range(0, n+1):
		s = getSentence(minwps)
		verse = createVerseFromSentence(s)
		if(len(verse) > maxwpl):
			tempstr = ''
			low = 0
			top = randint(minwpl, maxwpl)
			while(low < len(verse)):
				tempstr = ''
				for i in range(low, top):
					tempstr += verse[i] + ' '
				low = top
				newrand = randint(minwpl, maxwpl)
				top = top + newrand if (top + newrand < len(verse)) else len(verse)
				addToOutput(tempstr.strip(' '))
		else:
			addToOutput(' '.join(verse).strip())

def closeFileIO():
	f_output.close()
	f_feed.close()

def program():
	getVerses()
	prepareOutput()
	printOutput()
	closeFileIO()

program()