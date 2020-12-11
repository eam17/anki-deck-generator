# Generate Anki decks
import genanki

# Randomize the deck id
from random import randint


# Returs an random 11-digit number in order to not duplicate decks
def get_eleven_digits():
    value = randint(00000000000, 99999999999)
    return value


def construct_deck(text_file_name, image_names):
    deck = genanki.Deck(get_eleven_digits(), text_file_name)

    # Add images to the deck
    my_package = genanki.Package(deck)
    m_files = list()
    for name in image_names:
        m_files.append(name)
    my_package.media_files = m_files
    return deck


def create_model():
    model = genanki.Model(
        16073923129,
        'Word',
        fields=[
            {'name': 'Word'},
            {'name': 'Image'},
            {'name': 'Definition'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Word}}',
                'afmt': '{{Image}} <br> {{Definition}}'
            }]
    )
    return model

# Accepts a dataframe, generates an Anki deck in current dir
def get_pic_deck(df_esp_eng_img, text_file_name):
    # Generate an empty deck with images attached to it
    image_names = df_esp_eng_img['Image']
    deck = construct_deck(text_file_name, image_names)

    # Create a model to follow
    model = create_model()

    for index, row in df_esp_eng_img.iterrows():
        # print(row['Eng_words'])
        esp = row['Esp_words']
        print("row['Eng_words']: ", row['Eng_words'], type(row['Eng_words']))
        eng = "<br>".join(row['Eng_words'])
        img = row['Image']
        img_src = "<img src=" + img + ">"
        # Create a note
        note = genanki.Note(
            model=model,
            fields=[esp, eng, img_src]
        )

        # Insert the note into the deck
        deck.add_note(note)
    deck_name = text_file_name + "0.apkg"
    genanki.Package(deck).write_to_file(deck_name)
