# lang-read-assist
Translate portions of a body of text to a target language to make reading easier. 

## Objective 
We are given two texts, and the objective is to be able to translate a specific word or phrase of the first text to its corresponding word in the second text.

The underlying principle is that context becomes easier to understand as you understand more words in a text. Thus, by taking words in a target language and translating some % of them (more generally, some subset of them), we can understand more of the target language passage while still achieving the general benefits of reading in a target language. See below for example.

## Example
Given this text in Persian,

توانا بود هرکه دانا بود

We want to be able to define a % of the text to translate, and also be able to translate specific words after at ease.

For a persian-english translation at a 5% assistance level, the program might output:

توانا بود هرکه دانا بود
بود knowledge توانا بود هرکه

We can determine the order by which words should be translated by checking their bucket position in a frequency list. The less common the bucket, the earlier the word is translated.


## Process
- Translate text A to text B using translation API.
- Individually translate each word in A to B. [wordreference style API providing all meanings]
	- The only valid translations will be those which already exist (at least synonymously) in B.
- Create a map of words from A to B from those individual translations.
