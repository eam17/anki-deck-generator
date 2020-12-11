# Read and write to files
import io

# Clean up text for lemmatization
import textacy.preprocessing

# Work with natural language text
import spacy
from spacy.symbols import nsubj, VERB

# Lets us male an API request
import requests

# Save translations between runs
import sqlite3

# Parse string into json object
import json

# Access the list of words to avoid
import learnedlisthelper


# Gets content prepared to be used
def get_content(text_file_name):
    # Import text
    with io.open(str(text_file_name + '.txt'), mode='r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    # Pre-process the text
    content = content.replace('\n', ' ')
    textacy.preprocessing.normalize.normalize_quotation_marks(content)
    textacy.preprocessing.normalize.normalize_hyphenated_words(content)
    textacy.preprocessing.normalize.normalize_whitespace(content)
    textacy.preprocessing.remove.remove_punctuation(content, marks="\"-'`")

    # Pass the content to be lemmatized
    return content


# Returns a dict of {'Freqs':[ints],'esp_words':[strs in esp]}
def get_ordered_lemmas(content, max_words):
    # Lemmatize  the text
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(content)

    # A list of words to avoid
    words_to_avoid = learnedlisthelper.return_list()

    verbs = list()

    only_words = {}  # dict of {'lemma':[freq]}
    # Filter out stop words, keep only real words
    for token in doc:
        if token.is_alpha is True and token.is_stop is False and token.pos_ not in ("PRON", "CCONJ", "PROPN", "DET"):
            lower_lemma = token.lemma_.lower()
            # Only put it into array if we're not supposed to avoid the word
            if lower_lemma not in words_to_avoid:
                if token.pos_ == 'VERB':
                    # print('token.head.pos: ', token.head.pos, type(token.head.pos))
                    # print('token.pos: ', token.pos, type(token.pos))
                    # print('token.pos_: ', token.pos_, type(token.pos_))
                    verbs.append(lower_lemma)
                if lower_lemma not in only_words:
                    only_words[lower_lemma] = 1
                else:
                    only_words[lower_lemma] += 1

    # Sort lemmas
    sorted_words = sorted(only_words.items(), key=lambda x: x[1], reverse=True)  # List of tuples in order

    print("len: ", len(verbs))
    # print verbs in order


    # Convert list of tuples into dict of arrays
    words_dict = {"Freqs": list(), "Esp_words": list(), 'Eng_words': list()}
    # Print sorted words here:
    # print('sorted_words', sorted_words, type(sorted_words))
    for i in range(max_words):
        # print('sorted_words[i]', sorted_words[i], type(sorted_words[i]))
        # print('sorted_words[i][1]', sorted_words[i][1], type(sorted_words[i][1]))
        words_dict["Freqs"].append(sorted_words[i][1])
        words_dict["Esp_words"].append(sorted_words[i][0])

    # # Add an extra 10 top used verbs
    # max_count = 0
    # for sorted_tuple in sorted_words:
    #     if sorted_tuple[0] in verbs:
    #         words_dict["Freqs"].append(sorted_tuple[1])
    #         words_dict["Esp_words"].append(sorted_tuple[0])
    #         max_count += 1
    #     if max_count > 9:
    #         break
    return words_dict


# Check for the translation in the database. If not found..
# ..Access the Merriam-Webster API to return an array or short definitions for word
def get_eng_array(word):
    # Connect to the database
    conn = sqlite3.connect('img_urls.db')
    c = conn.cursor()
    result = c.execute('SELECT * FROM translations WHERE lemma =?', (word,)).fetchall()

    # Try to retrieve translations from the db
    if len(result) > 0:
        # Already in db, don't call API again
        conn.close()
        # print('result: ', result, type(result))
        # print('result[0][1]: ', result[0][1], type(result[0][1]))
        # Grab the english translations as string
        transl_str = result[0][1]
        # Separate the string into an array or strings
        transl_arr = transl_str.split("*")

        # make sure it's not blank
        if len(transl_str) < 1:
            json_str = result[0][2]
            # Turn str back into json
            json_obj = json.loads(json_str)
            transl_arr = json_obj[1]['shortdef']
            print(word, " was blank, used second shortdef", ' transl_arr: ', transl_arr, type(transl_arr))

        # The else returns an array of arrays, do the same here - NO
        word_en_arr = list()
        for item in transl_arr:
            # While we're at it, get rid of weird records, like > [word : translation]
            clean_item = item.split(":")
            if len(clean_item) > 1:
                clean_item = clean_item[1]
            clean_item = "".join(clean_item)
            clean_item = clean_item.strip()
            # # Turn string into an array of one element
            # clean_item = [clean_item]
            word_en_arr.append(clean_item)
        return word_en_arr
    # Couldn't find translations in the db
    else:
        # Call API and then save in db
        api_key = '3d805e76-a019-4f9a-b9cf-1a812ae47b91'
        url = 'https://dictionaryapi.com/api/v3/references/spanish/json/' + word + '?key=' + api_key
        session = requests.Session()
        r = session.get(url)
        # Make sure we get a successful response before continuing
        if r.status_code != 200:
            print("M-W returned ", r.status_code, " for ", word)
            conn.close()
            exit()
        else:
            word_en_arr = list()

            # Response as a json
            json_obj = r.json()
            try:
                # Some jsons return as random arrays..
                # They seem to contain words we can find
                if isinstance(json_obj[0], dict) is False:
                    print(word, " doesn't return nicely from M-W, isn't a dict. Looking at first element of array instead..")
                    print('json_obj: ', json_obj, type(json_obj))
                    print('json_obj[0]: ', json_obj[0], type(json_obj[0]))
                    print('type(json_obj[0]): ', type(json_obj[0]), type(type(json_obj[0])))
                    return get_eng_array(json_obj[0])

                # Populate an array containing arrays of translations
                word_en_arr = json_obj[0]['shortdef']
                arr_as_str = "*".join(word_en_arr)
                json_str = r.text
                c.execute('INSERT INTO translations VALUES (?,?,?)', (word, arr_as_str, json_str))
                print("Inserted new translation into db")
            except:
                print("Error in get_eng_array(word) when dealing with json")
                print("word:", word)
                print('json_obj[0]: ', json_obj[0], type(json_obj[0]))
                print('json_obj: ', json_obj, type(json_obj))
                print('r.text: ', r.text, type(r.text))
                print('json_obj[0][0]: ', json_obj[0][0], type(json_obj[0][0]))
            finally:
                conn.commit()
                conn.close()
            return word_en_arr


# Accepts a dict of freqs and spanish lemmas, should populate the english column
def get_esp_eng_dict(lemmas_dict):
    no_eng = list()

    # Loop over every row
    for row in range(len(lemmas_dict["Esp_words"])):
        # Grab the spanish word we're on
        esp_word = lemmas_dict["Esp_words"][row]
        # Grab an array of translation for the word we're on
        eng_word_arr = get_eng_array(esp_word)

        # Insert the translation into the dict
        if len(eng_word_arr) > 0:
            lemmas_dict["Eng_words"].append(eng_word_arr)
        else:
            # Save a list of words without translations
            no_eng.append(esp_word)
    # Delete the esp word without eng translation from the dict - doesn't work??
    # convert to dataframe earlier..
    print(len(no_eng))
    for lonely_word in no_eng:
        print("Gonna remove ", lonely_word)
        print('lemmas_dict["Esp_words"]: ', type(lemmas_dict["Esp_words"]), lemmas_dict["Esp_words"])
        lemmas_dict["Esp_words"].remove(lonely_word)
        print('lemmas_dict["Esp_words"]: ', type(lemmas_dict["Esp_words"]), lemmas_dict["Esp_words"])
    return lemmas_dict


def translator_driver(text_file_name, max_words):
    # Grab cleaned text
    content = get_content(text_file_name)
    # Grab a dict of lemmas and frequencies, ordered by freq
    esp_lemmas = get_ordered_lemmas(content, max_words)
    # Grab a dictionary containing everything but images
    esp_eng_dict = get_esp_eng_dict(esp_lemmas)
    # Dict containing freq, esp, eng
    return esp_eng_dict
