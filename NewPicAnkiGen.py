import sys

import io

# Find and image matching to a keyword
from google_images_search import GoogleImagesSearch

# Character recognition tool
from PIL import Image
import pytesseract

# Overrides google img methods for better naming
import GoogleFix



print(sys.getdefaultencoding())
print("hello")

import lemmastranslator

#
# content = codecs.open('cats0.txt', mode='r', encoding='utf-8')

# with io.open('contentCats.txt', mode='w', encoding='utf-8') as file:
#     for lemma in content:
#         s = lemma + "\n"
#         file.write(s)
#     print("done")
#
#




esp_list = list()


# with io.open('lemmasFreqs.txt', mode='w', encoding='utf-8') as file:
#     sorted_words = lemmastranslator.get_ordered_lemmas(lemmastranslator.get_content("cats0"))
#     #print(type(sorted_words))
#     #print(sorted_words)
#     for i in range(len(sorted_words["Freqs"])):
#         msg = str(sorted_words["Esp_words"][i] + " : " + str(sorted_words["Freqs"][i]) + "\n")
#         #print(msg)
#         file.write(msg)
#         # esp_list.append(word[0])


# Grab cleaned text
content = lemmastranslator.get_content("cats0")
# Grab a dict of lemmas and frequencies, ordered by freq
esp_lemmas = lemmastranslator.get_ordered_lemmas(content, 5)
# Grab a dictionary containing everything but images
esp_eng_dict = lemmastranslator.get_esp_eng_dict(esp_lemmas)

with io.open('lemmasFreqsandTranslate.txt', mode='w', encoding='utf-8') as file:
    print("esp_eng_dict: ", type(esp_eng_dict))
    print(esp_eng_dict)
    for i in range(len(esp_eng_dict["Freqs"])):
        # print('esp_eng_dict["Freqs"][i]', esp_eng_dict["Freqs"][i], type(esp_eng_dict["Freqs"][i]))
        msg = str(str(esp_eng_dict["Freqs"][i]) + " : " + esp_eng_dict["Esp_words"][i] + " : " + "* *".join(esp_eng_dict["Eng_words"][i]) + "\n")
        print(msg)
        file.write(msg)
exit()

# Translate lemmas, keep successful ones, keep tuples (es, en)
import json



def test1():

    word = 'parecer'



    # print("code: " + str(r.status_code))
    # print("text: " + r.text)

    #
    # print(type(json_obj[0]))
    #
    # print(type(word_en_arr))
    # print(word_en_arr)


# shortdef

# Grab top 25, find pics from english
# grab the first short def
search_img_str = 'to seem'  # word_en_arr[0].split(',')[0]
print(type(search_img_str), ", ", search_img_str)

# search first, then download and resize afterwards:

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch('AIzaSyCgzwvuTHnAOvQ65tAfNplAlLPSZVKxGaE', '002835885342643820817:bsi9ysot7kw')

# GoogleImagesSearch.download_image = GoogleFix.download_image
# GoogleImagesSearch._get_all_items = GoogleFix._get_all_items
# GoogleImagesSearch.download = GoogleFix.download





import os

path = os.getcwd() + "\\" + text_file_name + "Images\\"
os.makedirs(path, exist_ok=True)

# Look up all words and save them to a folder
# need to keep track of images we already tried..
# keep tried urls in csv
for image in gis.results():
    print(len(gis.results()))
    print(type(image))

    url_str = str(image.url)
    if CheckUrls.should_save(url_str, image) is False:
        continue
    else:
        file_name = str("".join(search_img_str.split()) + ".jpg")
        full_path = str(path + file_name)

        # Save the image at a specified url
        urllib.request.urlretrieve(url_str, full_path)

        # Open it back up for resizing
        image = Image.open(full_path)
        image.thumbnail((400, 400))
        image.save(full_path)
        print("size: ", image.size)

img = Image.open("img/como.jpg")
print("img open")
text = pytesseract.image_to_string(img, lang="eng+spa")
print(text)
print(len(text))


# instead, save images with the word being their name. Manually get rid of the pics with words
# scan the folder, if one of the words in the list doesn't have an image, find another one?

# Store in a dataframe
# Accepts an array of strings for spanish words and an array or arrays for english
# Returns a df with a spanish lemma, an array of translations and an image. If image is null, go get one?
def construct_df(words_esp_arr, words_eng_arr):
    # First let's populate what we have so far
    print()
# lets get an array of images

# spanish str, english list of strs,

# Construct a deck from the dataframe
