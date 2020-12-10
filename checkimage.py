# take a url, check if it's in our csv
# if it is, return false
# if it's not, add to csv and return true

# In the the file, if we're on the last image, expand the search result. Make it bigger already
import csv

import pytesseract

# Save data between runs
import sqlite3

import io


def should_save(url, folder):
    # Check what's already in the file
    # Connect to the database
    conn = sqlite3.connect('img_urls.db')
    c = conn.cursor()
    result = c.execute('SELECT * FROM urls WHERE href =?', (url,)).fetchall()
    if len(result) > 0:
        print("Don't save the image")
        conn.close()
        return False
    else:
        # Url is not in file. Add it
        c.execute('INSERT INTO urls VALUES (?)', (url,))
        print("added stuff")
    conn.commit()
    conn.close()

    # Next check if theres any text on the image
    # grab the string from the image
    text = ""  # pytesseract.image_to_string(image, lang="eng+spa")

    # No text on the image, please
    if len(text) > 1:
        return False
    else:
        return True
