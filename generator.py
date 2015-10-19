#  Atrus script

import re
import random
import math
from random import randint

# -- BEGIN MODIFIABLE VARIABLES --

u_output = "output.txt" # file used for the output
u_input = "atrus.txt" # file used for the input (the list of sentences)
sig = "\n#PoemsFromAtrus" #  signature put at the end of the tweet
n = 5 # num sentences
rm = 1 # random modifier
minwps = 3 # minimum words per sentence
minwpl = 5 # minimum words per line
maxwpl = 8 # maximum words per line
lc = 1 # last cap bool
li = 0 # last sentence index
clim = 140 - len(sig) # tweet character limit
uclim = 1 # whether or not to character limit

#  -- END MODIFIABLE VARIABLES --

f_output = open(u_output,'w') # output file
f_feed = open(u_input,'r') # input file
r_feed = f_feed.read() # read contents of input file

punc = ["?", "--", ".", ",", "!", " ", ";", ".", " ", "..."] # list of puncation
puncRequireCap = ["?", ".", "!", ":", ";"] # list of punctuation that requires capitalized letter after
sentences = list(re.split(r' *[\.\?!][\'"\)\]]* *', r_feed)) # list of sentences
pNouns = ["catherine", "atrus", "achenar", "sirrus", "d'ni", "i"] # list of names/proper nouns

oBuffer = [] # output buffer
oString = "" # final output string
fcnt = 0 # final character count
rccnt = 0 # running character count

def addToOutput(segment):
	global rccnt
	oBuffer.append(segment)
	rccnt += len(segment)

def prepareOutput():
	global oString
	oString = "\"" + "\n".join(oBuffer).strip(' ') + "\"" + "\n" + sig
	f_output.write(oString)

def printOutput():
	print(oString)

def createSentence():
	global li
	s = []
	ni = randint(0, len(sentences)-1) # new index

	if(rm):
		while((ni == li) or (ni + 1 == li) or (ni - 1 == li)):
			ni = randint(0, len(sentences)-1)
		li = ni
		s = list(sentences[li].split(' '))
	else:
		s = list(random.choice(sentences).split(' '))
	p = random.choice(punc)
	lw = str(s[len(s)-1]+p)
	s[len(s)-1] = ''.join(lw)
	return s

def modifyFirstChar(verse):
	ffw = ''; # final first word
	ofw = verse[0] # original first word of verse
	ofl = ofw[0] # original first letter of verse
	iofw =  ofw[1:len(verse[0])] # original first word minus first letter

	if (lc == 1 or ofw.lower() in pNouns):
		ffw = ''.join(ofl.upper() + iofw)
	else:
		ffw = ''.join(ofl.lower() + iofw)
	return ffw

def setLastCapGlobal(verse):
	global lc
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
	global rccnt
	global fcnt

	for _ in range(0, n+1):
		s = getSentence(minwps)
		v = createVerseFromSentence(s)
		ml = math.ceil(len(v) / minwpl) if (len(v) > minwpl) else 1 # get max num of lines possible
		checkmax = (rccnt + 2 + len(' '.join(v).strip(' ')) + ml + len(oBuffer)) # check the current max (+ possible upper limit) num of characters at the moment
		if(not uclim or (uclim and checkmax < clim)):
			if(len(v) > maxwpl):
				tempstr = ''
				low = 0
				top = randint(minwpl, maxwpl)
				while(low < len(v)):
					tempstr = ''
					for i in range(low, top):
						tempstr += v[i] + ' '
					low = top
					newrand = randint(minwpl, maxwpl)
					top = top + newrand if (top + newrand < len(v)) else len(v)
					addToOutput(tempstr.strip(' '))
			else:
				addToOutput(' '.join(v).strip())
		elif(uclim and len(oBuffer) == 0):
			rccnt = 0
		elif(uclim):
			fcnt = len("\"" + "\n".join(oBuffer) + "\"" + "\n" + sig) # final char count
			print("Breaking: Character count = " + str(fcnt) + "\n")
			break

def closeFileIO():
	f_output.close()
	f_feed.close()

def program():
	getVerses()
	prepareOutput()
	printOutput()
	closeFileIO()

program()