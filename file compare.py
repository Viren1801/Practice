import csv
import inflect
import numpy as np

indexed = []
list2 = []
p = inflect.engine()
with open(r"E:\slurrp cleaning\unique_indexed_ingredients.csv", "r", newline="", encoding='utf8') as file:
    reader = csv.reader(file)
    for row in reader:
        indexed.append(row[0])

with open(r"E:\slurrp cleaning\unique_search_ingredients.csv", "r", newline="", encoding='utf8') as file:
    reader = csv.reader(file)
    for row in reader:
        list2.append(row)

# converting the list from 2d to 1d
searching = [j for sub in list2 for j in sub]

individual_indexed_words = []
for sentence in indexed:
    for word in sentence.split():
        word = word.lower()
        if word not in individual_indexed_words:
            try:
                word_flag = p.singular_noun(word)
                if word_flag:
                    word = word_flag
            except:
                pass
            individual_indexed_words.append(word)
# print(individual_indexed_words)

individual_searched_words = []
for sentence in searching:
    for word in sentence.split():
        word = word.lower()
        if word not in individual_searched_words:
            try:
                word_flag = p.singular_noun(word)
                if word_flag:
                    word = word_flag
            except:
                pass
            individual_searched_words.append(word)
print(individual_searched_words)

junk_data = []
for word in individual_searched_words:
    if word not in junk_data:
        if word not in individual_indexed_words:
            junk_data.append(word)

with open(r'E:\slurrp cleaning\junk.csv', 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    for i in junk_data:
        writer.writerows([[i]])

print(junk_data)
