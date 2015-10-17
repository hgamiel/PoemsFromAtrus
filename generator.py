# Atrus script

import re
import random
from random import randint

f_output = open('output.txt','w')
f_feed = open('atrus.txt','r')
r_feed = f_feed.read()

punc = ["?", "--", ".", ",", "!", " ", ";", ".", " "]
sentences = list(re.split(r' *[\.\?!][\'"\)\]]* *', r_feed))
names = ["catherine", "atrus", "achenar", "sirrus"]

lc = 1 #last cap bool
lastIndex = 0 #last sentence index

def writeAndPrint(line):
	f_output.write(line + "\n")
	print(line)

def createSentence(freeverse):
	global lastIndex
	s = []
	newIndex = randint(0, len(sentences)-1)

	if(freeverse):
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

	if (lc == 1 or (ofl == "i" and len(ofw) == 1) or ofw.lower() in names):
		ffw = ''.join(ofl.upper() + iofw)
	else:
		ffw = ''.join(ofl.lower() + iofw)
	return ffw

def setLastCapGlobal(verse):
	global lc
	lastchar = verse[len(verse)-1][-1::]

	if (lastchar == '?' or lastchar == '.' or lastchar == '!' or lastchar == ":" or lastchar == ";"):
		lc = 1
	else:
		lc = 0

def getVerses(numverses, freeverse):
	lastRandomNum = 0

	for _ in range(0, numverses+1):
		s = createSentence(freeverse)
		if (len(s) > 2):
			verse = s
			verse[0] = modifyFirstChar(verse)
			setLastCapGlobal(verse)
			if(len(verse) > 8):
				tempstr = ''
				low = 0
				top = randint(5, 8)
				while(low < len(verse)):
					tempstr = ''
					for i in range(low, top):
						tempstr += verse[i] + ' '
					low = top
					newrand = randint(5, 8)
					top = top + newrand if (top + newrand < len(verse)) else len(verse)
					writeAndPrint(tempstr.strip(' '))
			else:
				writeAndPrint(' '.join(verse).strip())

def program():
	n = 5
	fv = 1
	#n = int(input("Please enter the number of verses you would like: "))
	#fv = int(input("Please enter '1' for freeverse or '0' for random chance of back-to-back lines: "))
	getVerses(n, fv)
	writeAndPrint("\n#PoemsFromAtrus")
	f_output.close()
	
	

program()