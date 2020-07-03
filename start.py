#Generate Anki decks
import genanki
#Regex matching
import re

#set up Anki elements
lang_names = {'en': 'English'}
name = "mydeck"
arr = ["first", "second", "third"]
string = "firstSen, secondSen, thridSen"
word = ''
definition = ""

#Read text from a file and split it into an array of sentences
with open('sample.txt', mode = 'r', encoding = ' ISO-8859-1') as file:
    content = file.read()
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', content)
words = re.split(r'(\b[^\s]+\b)', content)
#Use the sentences to generate an array of vocab words
countS = 0
vocab = []
for w in words:
        if w not in words:
            vocab.append(w)

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

print("done")
with open("new.txt", 'w') as f:
    for w in words:
        f.write(w + "\n")