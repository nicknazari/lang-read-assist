import translators as ts
import sys

# language codes
# english = en
# persian = fa
# spanish = es

def translate(text, nativelang, targetlang):
	return ts.google(text, nativelang, targetlang)

# need to write wrapper for wordreference api to get all possible translations of a word
def get_translations(word):
	translations = []
	# wordreference api call, append to translations each possibility
	return translations

filename = sys.argv[1]		# name of file
nativelang = sys.argv[2] 	# native language code
targetlang = sys.argv[3] 	# target language code
percent = sys.argv[4]		# percent of file to translate
# ie main.py mobydick_persian.txt fa en 20
# will give you top 20% of difficult words in mobydick_persian.txt translated to english

with open(filename, 'r') as f:
	text = f.read()

print(translate(text, nativelang, targetlang))
