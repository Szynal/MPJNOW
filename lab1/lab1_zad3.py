import re
import json
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
with open('wynik.json', 'r') as file:
    words = (" ").join(json.load(file)['slowa'])
with open('stopwords.txt', 'r') as file:
    sw = file.read().splitlines()
mask = np.array(Image.open(path.join(d, "maska.jpg")))
wc = WordCloud(background_color="white", max_words=2000, mask=mask)
wc.generate(words)
stopwords = set(STOPWORDS)
for s in sw:
    stopwords.add(s)
wc2 = WordCloud(background_color="white", max_words=2000, mask=mask,
               stopwords=stopwords)
wc2.generate(words)
wc.to_file(path.join(d, "mapa bez stopwordów.png"))
wc2.to_file(path.join(d, "mapa ze stopwordami.png"))

# Słowa znajdujące się w pliku stopwords nie znalazły się w drugiej z chmur
