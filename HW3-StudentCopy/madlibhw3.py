# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

print("START*******")
# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
from nltk.book import *
import random


# import nltk
#nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize

debug = False #True

string1 = (text2[:151])
joint = ' '.join(string1)
print (joint)

'''# get file from user to make mad lib out of
if debug:
	print ("Getting information from file text2.txt...\n")
fname = "madlibtest2.txt" # need a file with this name in directory

f = open(fname, 'r')
joint = f.read()'''

tokens = nltk.word_tokenize(joint)
tagged_tokens = nltk.pos_tag(tokens)

#print("TOKENS")
#print(tokens)

 # gives us a tagged list of tuples
#print("TAGGED TOKENS")
#print(tagged_tokens)
#if debug:
#	print ("First few tagged tokens are:")
#	for tup in tagged_tokens[:5]:
#		print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective","P":"Preposition"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "P":1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))

print("\n\nEND*******")

#
