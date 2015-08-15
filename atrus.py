# Atrus script

import re
import random
from random import randint

feed = "I realized, the moment I fell into the fissure, that the book would not be destroyed as I had planned. It continued falling into that starry expanse of which I had only a fleeting glimpse. I have tried to speculate where it might have landed, but I must admit, however- such conjecture is futile. Still, the question of whose hands might someday hold my Myst book are unsettling to me. I know that my apprehensions might never be allayed, and so I close, realizing that perhaps, the ending has not yet been written. Catherine, my love, I have to leave quickly. Something terrible has happened. It's hard for me to believe. Most of my books have been destroyed. Catherine, it's one of our sons. I suspect Achenar, but I-I shouldn't leap to conclusions. After it, it might have been Sirrus as well. Ah, I should have known not to have left my library unchecked for so long! Well, I've removed the remaining undamaged books from the library and placed them in the places of protection. You shouldn't have to use the books until I return, but... If you've forgotten the access key, remember the tower rotation. And, don't worry, Catherine, everything will be fine. I'll see you shortly. Oh, and... and erase this message after you've viewed it, just to be safe. Who the devil are you? D-Don't come here to D'ni-not yet. Oh, I have many questions for you, my friend, as you, no doubt, have for me. Where should I begin? Oh, perhaps my story is in order. My name is Atrus. I fear you have met my sons, Sirrus and Achenar, in the red and blue books, on Myst Island, in my library, my library... Oh, it contains my works, my writings. Oh, I wrote many books, many books that linked me to fantastic places. It's an Art I learned from my father many years ago. Oh, but the red and blue books, those were different. I wrote those books to entrap over-greedy explorers that might stumble upon my island of Myst. But I had no idea my own sons would be entrapped. My sons, Sirrus and Achenar, we had many journeys together. I gave them free reign to the books. Perhaps it was not wise. I could see the greed growing in them. I had not told them about the red and blue books. Their imaginations went wild; they dreamed of riches and power! Of course, they did not know the books were traps. They begged for access to those books and I, of course, denied them. Oh, they devised a plan, an evil plan. I had no idea to what extent their greed had... had... progressed. Their own mother-they used their own mother-Oh, my dear Catherine!-to lure me here to D'ni. Of course, I could return to Myst, except they removed a single page from my Myst Linking Book. I cannot return without that page-you, my friend, can bring that page to me. Oh, I pray you believe my story above the lies that my sons have told you. If you would find it in yourself to return that page to me here in D'ni, I could go to Myst, and bring justice to my sons for what they have done. I must return to my writing. I pray that you believe me. Please hurry. Bring the page. Bring the page with you. Have you found the missing page? Oh, come, come. Come on then. Ah, my friend. You've returned. We meet face-to-face. And the page, did you bring the page? You didn't bring the page. You didn't bring the page. What kind of FOOL are you?! Ah! Did you not take my warning seriously? *deep sigh* Welcome to D'ni. You and I will live here... forever. Ah, my friend. You've returned. And the page, did you bring the page? Ah, give it to me... Give me the page... Please, give the page... The page my friend, the page... [gives page]. You've done the right thing. I have a difficult choice to make. [puts page in book] My sons have betrayed me. I know what I must do. I shall return shortly. [links out]. [links in]. Hmm, it is done. I have many questions for you, my friend, but my writing can not wait. I fear that my long delay may have already had a catastrophic impact on the world in which my wife, Catherine, is now being held hostage. Oh, a reward, I'm sorry, but all I have to offer you is the library on the island of Myst and the books that are contained there. Feel free to explore at your leisure. I hope you find your explorations satisfying. You will no longer have my sons to deal with. Oh, and one more thing. I am fighting a foe much greater than my sons could even imagine. At some point in the future, I may find it necessary to request your assistance. Until that point, I'm afraid you'll enjoy the explorations from my library on Myst. Thank you. The book, you can use the Myst Linking Book to return to Myst."

punc = ["?", "--", ".", ",", "!", " ", ";", ".", " "]
sentences = list(re.split(r' *[\.\?!][\'"\)\]]* *', feed))

lastcap = 1
lastRandomNum = 0

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
					print(tempstr.strip(' '))
			else:
				print(' '.join(verse).strip())

def program():
	n = 5
	fv = 1
	#n = int(input("Please enter the number of verses you would like: "))
	#fv = int(input("Please enter '1' for freeverse or '0' for random chance of back-to-back lines: "))
	print("---#JustAtrusThings---\n")
	getverses(n, fv)
	print("\n-Atrus\n\n----------------------")

program()