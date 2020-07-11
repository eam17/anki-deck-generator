from __future__ import unicode_literals, print_function
#Generate Anki decks
import genanki
#Regex matching
import re
#Extracks verb phrases
import textacy


#set up Anki elements
lang_names = {'en': 'English'}
name = "mydeck"
arr = ["first", "second", "third"]
string = "firstSen, secondSen, thridSen"
word = ''
definition = ""

with open('sampleES.txt', mode = 'r', encoding = 'utf-8', errors='ignore') as file:
    content = file.read()


deck = genanki.Deck(2059406710, name)
model = genanki.Model(
    1607392319,
    'Word',
    fields=[
        {'name': 'Word'},
        {'name': 'Definition'},
        {'name': 'Examples'}
        ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Word}}',
            'afmt': '<b>{{FrontSide}}: </b> {{Answer}} <br> <b> Example use: </b> <span id="ex">{{Examples}}</span> <script>var str = document.getElementById("ex").innerHTML; arr1 = str.split(","); var content = document.getElementById("ex").innerHTML = arr1[Math.floor(Math.random() * arr1.length)];</script>'
        }]
)

note = genanki.Note(
                model=model,
                fields=["What is the capital of Great Brittan?", "London", string]
                )
deck.add_note(note)


#genanki.Package(deck).write_to_file('output.apkg')



# Import the Spanish language class
import spacy
nlp = spacy.load('es_core_news_sm')
nlpEn = spacy.load('en_core_web_lg')




import plac
import unicodedata
import textacy.resources
import textacy.preprocessing


content = content.replace('\n', ' ')
#textacy.preprocessing.normalize.normalize_unicode(content, 'NFC')
textacy.preprocessing.normalize.normalize_quotation_marks(content)
textacy.preprocessing.normalize.normalize_hyphenated_words(content)
textacy.preprocessing.normalize.normalize_whitespace(content)
textacy.preprocessing.remove.remove_punctuation(content,marks="\"-'`")
#print(unicodedata.is_normalized('NFC', content))
docEn = nlpEn(content)
#print(content)


count = 0
onlywords = list()

for token in docEn:
  if token.is_alpha == True and token.is_stop == False and token.pos_ not in ("PRON", "CCONJ", "PROPN", "DET"):
    #for chunk in doc.noun_chunks:
      #if token.text in chunk.text:
        #print(chunk)
    #for t in docEn:
      #if token.text == t.text:
        #if t.dep_ in ("xcomp", "ccomp","acl","advcl","csubj"):
          #s = "".join(w.text_with_ws for w in t.subtree) + " - " + str(count) + "\n"
          #print(s)
    if token.lemma_ not in onlywords:
      #print(count, "-", token.lemma_, token.pos_)
      onlywords.append(token.lemma_)
      count += 1

onlywords.sort()

with open('lemma.txt', mode = 'w') as file:
  for lemma in onlywords:
    s = lemma + "\n"
    file.write(s)
  file.write(str(count))

for w in docEn:
  if w.text == "corpulento":
    print(w.pos_)

#matcher
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)
pattern = [{"POS": "DET", "OP": "?"}, {"POS": "NOUN"},  {"POS": "ADJ"}]
matcher.add('nouns', None, pattern)
matches = matcher(docEn)

with open('phrases.txt', "w") as file:
  for match_id, start, end in matches:
     span = docEn[start:end]
     input = span.text + " " + docEn[start].pos_ + " " + "\n"
     file.write(input)


#gather short sentences of the text
count = 0
shortSents = list()

with open('shortsents.txt', 'w') as f:
  for sent in docEn.sents:
    if len(sent.text) < 60 and len(sent) > 5:
      shortSents.append(sent)
      s = sent.text + "\n"
      f.write(s)
      count += 1


print(count)