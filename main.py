from translate import Translator
import sys

# sys.argv[1] can be language
# sys.argv[2] can be document to translate
# sys.argv[3] can be optional argument for percent of document to translate. default is 100

# persian = fa
# spanish = es

def translate(text, nativelang, targetlang):
	translator = Translator(provider="libre", from_lang=nativelang, to_lang=targetlang)
	translation = translator.translate(text)
	return translation

# need to write wrapper for wordreference api to get all possible translations of a word
def get_translations(word):
	translations = []
	# wordreference api call, append to translations each possibility
	return translations

nativelang = sys.argv[1] # native language code
targetlang = sys.argv[2] # target language code

with open(sys.argv[3], 'r') as f:
	text = f.read()

print(translate(text, nativelang, targetlang))
