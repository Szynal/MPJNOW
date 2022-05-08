from os import listdir
from os.path import isfile, join
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import json

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

# print(texts)
with open('zad1_output/texts.json', 'w') as f:
    json.dump(texts, f)

# print(filtered_tokens)
with open('zad1_output/filtered_tokens.json', 'w') as f:
    json.dump(filtered_tokens, f)

# print(stemmed_tokens)
with open('zad1_output/filtered_tokens.json', 'w') as f:
    json.dump(stemmed_tokens, f)

# print(lematized_tokens)
with open('zad1_output/lematized_tokens.json', 'w') as f:
    json.dump(lematized_tokens, f)
