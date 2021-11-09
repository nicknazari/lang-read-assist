from bs4 import BeautifulSoup
import requests

engToSpanURL = "https://www.wordreference.com/es/translation.asp?tranword="
spanToEngURL = "https://www.wordreference.com/es/en/translation.asp?spen="

# will return a list of all WR given translations for word x
def wr_getwords(word, start_lang, target_lang):
	if start_lang == 'en' and target_lang == 'es':
		prefix = engToSpanURL	
	elif start_lang == 'es' and target_lang == 'en':
		prefix = spanToEngURL
	
	# 'payload' URL for which we will request: concat of prefix and word we need to request
	url = prefix + word
	r = requests.get(url)
	soup = BeautifulSoup(r.content)

	# NEXT STEP: find location of words in WR returned data
