from os import listdir
from os.path import isfile, join
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import KFold
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import numpy as np

print(f"Zad1 lab4 \n")

# Wczytaj dane z katalogów positive oraz negative z poprzedniego laboratorium
mypath = "data"
files_positive = [f for f in listdir(f"{mypath}/pos/") if isfile(join(f"{mypath}/pos/", f))]
files_negative = [f for f in listdir(f"{mypath}/neg/") if isfile(join(f"{mypath}/neg/", f))]
texts = []

for of in files_positive:
    with open(f"{mypath}/pos/{of}", "r") as f:
        texts.append(f.read())
for of in files_negative:
    with open(f"{mypath}/neg/{of}", "rb") as f:
        texts.append(f.read().decode("utf-8"))

# Dokonaj wektoryzacji z użyciem TfidfVectorizer

vectorization = TfidfVectorizer()
X = vectorization.fit_transform(texts)

# Utwórz tablicę etykiet (300 zer oraz 300 jedynek) typu ndarray
scores = np.zeros(5)
y = np.zeros(600)
y[0:300] = 1

# Dane podziel na 5 foldów z użyciem funkcji StratifiedKFold

kf = KFold(n_splits=5)

# Utwórz tablice na wyniki
# Dla każdego foldu:
# • Wytrenuj model z użyciem klasyfikatora MLPClassifier na danych treningowych (funkcja fit())
# • Dokonaj predykcji modelu na danych testowych (funkcja predict())
# • Zapisz w tablicy z punktu 5 dokładność wyrażoną za pomocą metryki accuracy_score
# Wyznacz średnią dokładność oraz odchylenie standardowe i wyświetl wyniki

for i, (train_index, test_index) in enumerate(kf.split(X)):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    clf = MLPClassifier(random_state=223)
    clf.fit(X_train, y_train)
    predict = clf.predict(X_test)
    scores[i] = accuracy_score(y_test, predict)

print(f"Average score: {scores.mean()} ({scores.std()})")
