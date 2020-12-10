# This driver script is responsible for calling correct methods and outputting a deck

# Populate folder with images of words
# Supply which file to read, expect to recieve a df(or dict) of esp+eng, and folder should be populated

# Refrain from defs in here..

# Process text file and output translations
import lemmastranslator

# Finds google images for words
import imagefinder

# Using dataframes
import pandas as pd

# Allows to execute system commands
import os

# Allows us to pause the application
import time

# Outputs an Anki deck
import deckgen

text_file_name = 'laisla'
max_words = 100

# dictionary of {'Freqs':[ints],'Esp_words':[strs in esp], 'Eng_words':[[strs separated by commas], 'Images':[]]}
esp_eng_dict = lemmastranslator.translator_driver(text_file_name, max_words)

df_esp_eng = pd.DataFrame(esp_eng_dict, columns=['Freqs', 'Esp_words', 'Eng_words'])

print(df_esp_eng)

# Add a new column full of empty strings
df_esp_eng['Image'] = [""] * df_esp_eng.shape[0]

# print(df_esp_eng)
# print("df_esp_eng['Image'][0]: ", df_esp_eng['Image'][0], type(df_esp_eng['Image'][0]), len(df_esp_eng['Image'][0]))

# Construct the path to the folder the images for this deck should be in
# Path to collections.media
path = 'C:\\Users\\Kat\\AppData\\Roaming\\Anki2\\User 1\\collection.media\\'
# Try tr create the folder in case it doesn't exist yet
os.makedirs(path, exist_ok=True)

# Populate the dataframe with images for the first time
df_esp_eng_img = imagefinder.add_images(df_esp_eng, path)

while df_esp_eng_img is None:
    time.sleep(15)


# print(df_esp_eng_img)

deckgen.get_pic_deck(df_esp_eng_img, text_file_name)

print("Done")