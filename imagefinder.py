# Using dataframes
import pandas as pd

# Allows to execute system commands
import os

# Find and image matching to a keyword
from google_images_search import GoogleImagesSearch
from google_images_download import google_images_download
from simple_image_download import simple_image_download

# User class for ensuring better image results
import checkimage

# Saves images to system from url
import urllib.request

# Allows to open and operate on an image
from PIL import Image

# Allows us to pause the application
import time


# Searches Google Images for 10 images for the specified search_term and downloads one
# If we haven't tried this image yet and it doesn't appear to have text, save it into the specified folder
# The name of the file will become search_term.png
def find_img_for_str(search_term, folder):
    # # Authenticate with the API
    # key = '\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDQ9CP/EcDhUC5D\\n/uJ3CqrKAg8cJ3ITQta0upxPfqiKeXkVcDwNkE9mU/VKa+4QYUpwyqJd2VOD2s1Z\\nz5F2qj1d/3CG+ZitOcCRuuBqK1Slk4BrPcJyDSQ3I68gF4XCz5zzoOSn6MXFdovI\\n3nxW0qz7lEY7Q2BjmeqvxiS6VEhM6RTBk/f7Gh7v00XL8lU92fTgYkO+t39oCkaN\\nxx065mZ+WAti7j1qcIK6CC0qCG5OXNXTPaxbR1x4PxTa4J8BFHG72j2afDo4qqCj\\nRjb8wedcjG9MOoM2V+zIUkc37AKjJRno9q2exMQWaGkJY8gxxCXj5T6bzasHw1QB\\n6ch1rugnAgMBAAECggEAAw9K0PsHPQVkjWBXxpskYcLin8Hqx2IXghv9b/iQf+lE\\nHvk+worAxDnUggYkkp7Uwo66Y+9rwVGHPO/E1zJU+wxjhHEhODV79BECz5XaLnaD\\neePfS2DqjS17l1e2K2Jzj5RlOhmMKSu8OPEbwasMwhOrbPC795loY1yJFdASzaAm\\nr0nF1zBU+wgKO8O5KLhBw0JqkCvOwMQMX4edsUlWW9Hj0s01zqkjnemFWFdMrHbS\\n3gdgVXnzHPrFsGsx8Yk2bpQMF4OTM980YBFDcSfCthnv4DMzY7AjRbx3abnUXh88\\nE+GEEEt7Y4ybCvXuvkDFjdHfVnEk9+2THMXf5+sSGQKBgQDoGLIt79M+oiEDggsZ\\nwN1zGIUF18P0lTUz2UgVPlZbt80hsJ7621jHPBFOpy1CzSojxn7kTaLxeqV/MwyJ\\n+FFiQWmeDdC8kFZxP7CYTYlPZAkeyvcuuOWprIZPU80PyeLwj4QUuO96VuP7nTax\\ny5yIPShYIc6CGc/hFzaP9yRuPQKBgQDmeUbbTgJzorK4yC5MtZswXs1fW20dp6uZ\\ncS/VVA0/Mj8/lhzyY0UB5x6i+MUGZjYp8/XnZHD0NnNCdvQV5/9yDqFZr8sLRsOf\\n44wluxUPsY9TIs9Pc4ZHlpNgJIXki6YN16TwzQ6MQHPRwDY8fwD8ugI3OIMYo0qU\\nWMlE/5HaMwKBgQDINKVeYsXB/XCk6gRRTsC3i6sTgy+RRzQBaah4SrGLpFzadtRs\\nZ9GI6xOy2Rp9ySRUf+DtZtrrmnQv6QUj7oOlUe+dWyV3wroOLnZSqm+LgCst2L6o\\nGu5hEmU5AHye5fNQtzuj9HL/APzgCpknfQ+lpbural4Mc9+RtshmHzXZsQKBgA+u\\nUrbbIOmTOUu/Ov83H/7zhE+nnc31uYQwIkwGcvxIw+rkoMWRIYHWosv91xHvZGII\\nWkPLHrBPABqWk1bmOQgenLXIcy0qPGcliUSL7QvrTdAfPzGtr4YxZYeWFJIPOlYY\\nxP0pRoMeY4Ly6/3DumJ3mWz+aFUFzy42uEL8jITnAoGAUbzhaofwYwziFSpsaMht\\nCmbDq3E/D1jfWU9BUl+/oL8Y1DP4wNyDpYglx080C20c+ZX5pM3T2UyFA1olJ1bB\\ngEnDT8izC0B8Fe5I0SGUZhYUpYASEb4j1wci7CSHJSvYVR2oxBKAXuu7Z4JNAF4l\\nT+Rf2/ICOhkM8a6/xVQCAnI='
    # short_key = '40d62f613e9165bb91dd2d62132682cceeed7c08'
    # gis = GoogleImagesSearch(short_key, 'cce2104d5e2e3f24a')
    #
    # _search_params = {
    #     'q': search_term,
    #     'num': 10,
    #     'safe': 'medium',
    #     'fileType': 'png',
    # }
    # # Preform the search
    # gis.search(search_params=_search_params)

    # path_to_chrome = 'C:\\Users\\Kat\\Documents\\'
    #
    # response = google_images_download.googleimagesdownload()  # class instantiation
    # arguments = {"keywords": search_term, "limit": 10, "download": True, "print_urls": True, "chromedriver": path_to_chrome}
    # paths = response.download(arguments)
    # print('search_term: ', search_term, type(search_term))
    # print('paths: ', paths, type(paths))

    response = simple_image_download.simple_image_download

    result = response().urls(search_term, 15,  extensions={'.jpg', '.png', '.jpeg'})

    # Loop over each image of the result
    for url in result:
        print(url)
        # If the image doesn't meet requirements, try the next one
        if checkimage.should_save(url, folder) is False:
            continue
        else:
            file_name = str("".join(search_term.split()) + ".png")
            full_path = str(folder + file_name)

            # Save the image at a specified url
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(url, full_path)

            # Open it back up for resizing
            image = Image.open(full_path)
            image.thumbnail((400, 400))
            image.save(full_path, headers={'User-Agent': 'Mozilla/5.0'})

            # Attempt to reduce the amount of HTTPS errors by pausing
            time.sleep(5)

            return
    # Something went wrong when looking for an image
    print("Could not find an image for ", search_term)
    exit()


# Accepts a dictionary, populates a dataframe with images where needed
def add_images(df_esp_eng_img, path):
    # Check what images we already have in the folder
    names_in_folder = os.listdir(path)
    # print('path: ', path, type(path))
    # print('names_in_folder: ', names_in_folder, type(names_in_folder))

    # Keep track of if we need to manually look at images again
    should_exit = False

    # Loop over each item in the Eng_words column
    index = 0
    for cell in df_esp_eng_img['Eng_words']:
        # Grab the first short def, don't remove the space yet, we need to search with it
        print('cell: ', cell, type(cell))
        search_img_str = str("".join(cell[0]).split(',')[0])
        # Get rid of parenthesis too
        search_img_str = str("".join(search_img_str.split('(')[0]))
        # This would be the file name, if it exists
        file_name = str("".join("".join(search_img_str).split(" ")) + ".png")
        # Decides if an image needs to be downloaded
        if file_name not in names_in_folder:
            # Means that we need to download an image for this word
            find_img_for_str(search_img_str, path)
            should_exit = True
            print('file_name: ', file_name, type(file_name))
        else:
            # Load the image file name into the dataframe
            column = df_esp_eng_img['Image']
            column[index] = file_name
        index += 1

    if should_exit:
        print("New images added to ", path, "\nRerun deckdriver.py")
        exit()
    return df_esp_eng_img
