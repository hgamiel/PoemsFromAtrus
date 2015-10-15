# Atrus script

import re
import random
from random import randint

f = open('output.txt','w')
f_feed = open('atrus.txt','r')
r_feed = f_feed.read()

punc = ["?", "--", ".", ",", "!", " ", ";", ".", " "]
sentences = list(re.split(r' *[\.\?!][\'"\)\]]* *', r_feed))

lastcap = 1
lastRandomNum = 0

def writeAndPrint(line):
	f.write(line + "\n")
	print(line)

def createSentence(freeverse):
	s = []
	global lastRandomNum
	if(freeverse):
		newRandomNum = randint(0, len(sentences)-1)
		lastRandomNum = newRandomNum if (newRandomNum != lastRandomNum) or (newRandomNum + 1 == lastRandomNum) or (newRandomNum - 1 == lastRandomNum) else randint(0, len(sentences)-1)
		s = list(sentences[lastRandomNum].split(' '))
	else:
		s = list(random.choice(sentences).split(' '))
	p = random.choice(punc)
	lw = str(s[len(s)-1]+p)
	s[len(s)-1] = ''.join(lw)
	return s

def modifyFirstChar(verse):
	firstChar = '';
	fw = verse[0].lower()
	fl = fw[0]
	if (lastcap == 1 or (fl == "i" and len(fw) == 1) or fw == "catherine" or fw == "atrus" or fw == "achenar" or fw == "sirrus"):
		firstChar = ''.join(verse[0][0].upper() + verse[0][1:len(verse[0])])
	else:
		firstChar = ''.join(verse[0][0].lower() + verse[0][1:len(verse[0])])
	return firstChar

def setLastCapGlobal(verse):
	lastchar = verse[len(verse)-1][-1::]
	global lastcap
	if (lastchar == '?' or lastchar == '.' or lastchar == '!' or lastchar == ":" or lastchar == ";"):
		lastcap = 1
	else:
		lastcap = 0

def getverses(numverses, freeverse):
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
	writeAndPrint("---#JustAtrusThings---\n")
	getverses(n, fv)
	writeAndPrint("\n-Atrus\n\n----------------------")
	f.close()
	
	

program()