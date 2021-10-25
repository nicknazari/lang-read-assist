# lang-read-assist
Translate portions of a body of text to a target language to make reading easier. 

## Objective 
We are given two texts, and the objective is to be able to translate a specific word or phrase of the first text to its corresponding word in the second text.

The underlying principle is that context becomes easier to understand as you understand more words in a text. Thus, by taking words in a target language and translating some % of them (more generally, some subset of them), we can understand more of the target language passage while still achieving the general benefits of reading in a target language. See below for example.

## Example


## Process
- Translate text A to text B using translation API.
- Individually translate each word in A to B. [wordreference style API providing all meanings]
- Create a map of words from A to B from those individual translations.

