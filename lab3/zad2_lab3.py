from os import listdir
from os.path import isfile, join
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import Counter
from pandas import DataFrame
import json

print(f"Zad2 lab4 \n")

mypath = "data"
stopwords = stopwords.words('english')
stemmer = PorterStemmer()
wnl = WordNetLemmatizer()

onlyfiles_p = [f for f in listdir(f"{mypath}/pos/") if isfile(join(f"{mypath}/pos/", f))]
onlyfiles_n = [f for f in listdir(f"{mypath}/neg/") if isfile(join(f"{mypath}/neg/", f))]
texts = []

for of in onlyfiles_p:
    with open(f"{mypath}/pos/{of}", "r") as f:
        texts.append(f.read())

for of in onlyfiles_n:
    with open(f"{mypath}/neg/{of}", "r") as f:
        texts.append(f.read())

filtered_tokens = []
stemmed_tokens = []
lematized_tokens = []

for i in range(len(texts)):
    texts[i] = texts[i].lower()
    texts[i] = TreebankWordTokenizer().tokenize(texts[i])
    filtered_text = [w for w in texts[i] if not w.lower() in stopwords]
    filtered_tokens.append(filtered_text)
    singles = [stemmer.stem(token) for token in filtered_text]
    stemmed_tokens.append(singles)
    singles_lem = [wnl.lemmatize(token) for token in filtered_text]
    lematized_tokens.append(singles_lem)

bag_tokens = []
bag_filtered = []
bag_stemmed = []
bag_lemmatized = []

for i in range(len(texts)):
    bag_tokens.append(Counter(texts[i]))
    bag_filtered.append(Counter(filtered_tokens[i]))
    bag_stemmed.append(Counter(stemmed_tokens[i]))
    bag_lemmatized.append(Counter(lematized_tokens[i]))

bag_tokens = DataFrame.from_records(bag_tokens)
bag_tokens.fillna(0, inplace=True)
bag_filtered = DataFrame.from_records(bag_filtered)
bag_filtered.fillna(0, inplace=True)
bag_stemmed = DataFrame.from_records(bag_stemmed)
bag_stemmed.fillna(0, inplace=True)
bag_lemmatized = DataFrame.from_records(bag_lemmatized)
bag_lemmatized.fillna(0, inplace=True)

bag_tokens = bag_tokens.to_numpy()
bag_filtered = bag_filtered.to_numpy()
bag_stemmed = bag_stemmed.to_numpy()
bag_lemmatized = bag_lemmatized.to_numpy()

# print(bag_tokens)
with open('zad2_output/bag_tokens.txt', 'w') as f:
    json.dump(bag_tokens, f)

# print(bag_filtered)
with open('zad2_output/bag_filtered.txt', 'w') as f:
    json.dump(bag_filtered, f)

# print(bag_stemmed)
with open('zad2_output/bag_stemmed.txt', 'w') as f:
    json.dump(bag_stemmed, f)

# print(bag_lemmatized)
with open('zad2_output/bag_lemmatized.txt', 'w') as f:
    json.dump(bag_lemmatized, f)
