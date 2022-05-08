from os import listdir
from os.path import isfile, join
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import Counter
from pandas import DataFrame
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

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

y = np.zeros(600)
y[300:] = 1
clf = MultinomialNB()
X_train, X_test, y_train, y_test = train_test_split(bag_tokens, y, test_size=0.3, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Dokadnosc(tokeny): {accuracy:.5f}")

X_train, X_test, y_train, y_test = train_test_split(bag_filtered, y, test_size=0.3, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Dokadnosc(filtrowane): {accuracy:.5f}")

X_train, X_test, y_train, y_test = train_test_split(bag_stemmed, y, test_size=0.3, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Dokadnosc(stemmed): {accuracy:.5f}")

X_train, X_test, y_train, y_test = train_test_split(bag_lemmatized, y, test_size=0.3, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Dokadnosc(lemmatized): {accuracy:.5f}")
