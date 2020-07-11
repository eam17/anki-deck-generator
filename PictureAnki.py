from google_images_search import GoogleImagesSearch
import spacy
import textacy
import textacy.resources
import textacy.preprocessing
import unicodedata

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch('AIzaSyCgzwvuTHnAOvQ65tAfNplAlLPSZVKxGaE', '002835885342643820817:bsi9ysot7kw')


nlp = spacy.load('es_core_news_sm')

# Get a list of vocab from anki export
with open("deck.txt", "r") as file:
    content = file.read()

content = content.replace('\n', ' ')
textacy.preprocessing.normalize.normalize_quotation_marks(content)
textacy.preprocessing.normalize.normalize_hyphenated_words(content)
textacy.preprocessing.normalize.normalize_whitespace(content)
textacy.preprocessing.remove.remove_punctuation(content,marks="\"-'`")

words = content.split(" ")

# Find images matching words
for word in words[1:]:
    # define search params:
    _search_params = {
        'q': word,
        'num': 1,
        'safe': 'medium',
        'fileType': 'jpg',
        }
    #print(word)
    gis.search(search_params=_search_params, path_to_dir='C:/Users/Kat/Desktop/Python Projects/FlashProj/anki-deck-generator/img')
# this will only search for images:
#gis.search(search_params=_search_params)

# this will search and download:
#gis.search(search_params=_search_params, path_to_dir='C:/Users/Kat/Desktop/Python Projects/FlashProj/anki-deck-generator/img')

# this will search, download and resize:
#gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500)

# search first, then download and resize afterwards:
#gis.search(search_params=_search_params)
#for image in gis.results():
    #image.download('/path/')
    #image.resize(500, 500)