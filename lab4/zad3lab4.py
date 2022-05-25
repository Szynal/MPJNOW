from os import listdir
from os.path import isfile, join
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

print(f"Zad3 lab4 \n")

# Dla poniższych wyrazów wyświetl statystyki TF-IDF na danych z poprzedniego zadania:
# • okręt
# • wiatr
# • fali
# • niebo
# • się
# Czy taka analiza statystyk dla wybranych słów pozwala na pewną kategoryzację dokumentów? Odpowiedź posze-
# rzoną o interpretację uzyskanych wyników, zapisz w postaci komentarza do kodu źródłowego.

mypath = "poezja"
onlyfiles = [f for f in listdir(f"{mypath}/") if isfile(join(f"{mypath}/", f))]
columns = []
texts = []

for of in onlyfiles:
    with open(f"{mypath}/{of}", "rb") as f:
        texts.append(f.read().decode("utf-8"))
    columns.append(' '.join(of.split('_')[2:]))

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
words = ['okręt', 'wiatr', 'fali', 'niebo', 'się']
df = pd.DataFrame(X.T.todense(), index=vectorizer.get_feature_names_out(),
                  columns=columns)
print(df.filter(items=words, axis=0))

# Interpretacja statystyk TFIDF pozwala na kategoryzację dokumentów, gdyż
# w tekstach o podobnej tematyce występują konkretne słowa. Przykładem może być
# słowo okręt, które ma wartość tfidf różną od 0 w przypadku tych tekstów
# które poruszają tematykę żeglugi. Natomiast nie należy podejmować tego typu
# wniosków na podstawie jednego słowa, gdyż wnioski tak poczynione mogą być
# błędne. Przykładem może być słowo fali, ktore pozwoliłoby na powiązanie
# tematyczne między utworami o tematyce morskiej ze Stepami Akermańskimi, które
# nie posiadają z nimi związku tematycznego.
