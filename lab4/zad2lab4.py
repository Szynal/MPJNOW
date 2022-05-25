from os import listdir
from os.path import isfile, join
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

# Wczytaj wszystkie dokumenty z katalogu poezja

mypath = "poezja"
onlyfiles = [f for f in listdir(f"{mypath}/") if isfile(join(f"{mypath}/", f))]
texts = []
for of in onlyfiles:
    with open(f"{mypath}/{of}", "rb") as f:
        texts.append(f.read().decode("utf-8"))

# Dokonaj wektoryzacji z użyciem TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Wylicz macierz podobieństw cosinusowych z użyciem cosine_similarity
cos_sim = cosine_similarity(X)
print(cos_sim)

# _____________________________________________________________________________________________________________

# 0.155 - 3x4
# 0.139 - 6x7
# 0.119 - 3x7

# Na wynik ma wpływ zarówno osoba autora jak i tematyka wiersza. Najwyższą wartość osiągnął wiersz o podobnej tematyce
# tego samego autora. Kolejny wynik osiągnął wiersz o innej tematyce tego samego autora, a trzeci najwyższy wynik
# osiągnął wiersz innego autora o tej samej tematyce
# _____________________________________________________________________________________________________________

# Wyznacz macierz odległości Euclidesowych z użyciem euclidean_distances
ed = euclidean_distances(X)
print(ed)

# _____________________________________________________________________________________________________________
# 1.406 - 5x4
# 1.403 - 5x2
# 1.400 - 5x3
# Największą odległość od wszystkich tekstów osiągnął tekst Jana Kochanowskiego, gdyż pochodzi on z innej epoki i używa
# innego słownictwa

# Podobieństwo kosinusowe oraz odległość euklidesowa wskazują na podobne wnioski. Teksty pochodzące od tego samego
# autora i z tej samej epoki są do siebie bardziej podobne pod kątem słownictwa.
# _____________________________________________________________________________________________________________
