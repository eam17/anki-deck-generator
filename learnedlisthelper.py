# Save learned words between runs
import sqlite3


# add a list of values as a string into the table
def add_to_list(input_str):
    input_arr = input_str.split(" ")

    conn = sqlite3.connect('img_urls.db')
    c = conn.cursor()

    count = 0
    for word in input_arr:
        result = c.execute('SELECT * FROM learned_words WHERE lemma =?', (word,)).fetchall()
        if len(result) == 0:
            c.execute('INSERT INTO learned_words VALUES (?)', (word,))
            count += 1
    conn.commit()
    conn.close()
    print("Added ", count, " words")
    return


# remove a list of values as a string from the table
def remove_from_list(input_str):
    input_arr = input_str.split(" ")

    conn = sqlite3.connect('img_urls.db')
    c = conn.cursor()

    count = 0
    for word in input_arr:
        result = c.execute('SELECT * FROM learned_words WHERE lemma =?', (word,)).fetchall()
        if len(result) > 0:
            c.execute('DELETE FROM learned_words VALUES (?)', (word,))
            count += 1
    conn.commit()
    conn.close()
    print("Removed ", count, " words")
    return


# remove all values from the table
def empty_list():
    conn = sqlite3.connect('img_urls.db')
    c = conn.cursor()

    count = 0
    result = c.execute('SELECT * FROM learned_words').fetchall()
    if len(result) > 0:
        for row in result:
            print('row[0]: ', row[0], type(row[0]))
            word = row[0]
            c.execute('DELETE FROM learned_words WHERE lemma =?', (word,))
            count += 1
    conn.commit()
    conn.close()
    print("Removed ", count, " words")
    return


# print all values in the table
def return_list():
    output_arr = list()
    conn = sqlite3.connect('img_urls.db')
    c = conn.cursor()
    result = c.execute('SELECT * FROM learned_words').fetchall()
    for row in result:
        print(row[0])
        output_arr.append(row[0])
    conn.close()
    return output_arr.copy()


# empty_list()

# input_str = "atrever"
# add_to_list(input_str)

# output_list = return_list()

# for i in output_list:
#     print(i)
