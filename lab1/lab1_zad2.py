import re
import json

with open('text.txt', 'r') as file:
    lines = file.readlines()
sentences = []
text = "".join(lines)


reg = re.compile(r'([A-ZŻŹĆĄŚĘŁÓŃ][^\.!?]*[\.!?])', re.MULTILINE)

sentences = reg.findall(text)
cleared_sentences = []
reg = re.compile(r'^(?!.*  ).+')
for i, sentence in enumerate(sentences):
    cleared_sentences.append(reg.findall(sentence)[0])
reg = re.compile(r'^(?!.*  ).+')
words = []
reg = re.compile(r'([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]*[^\.!?.\—,\,\n„ ])', re.MULTILINE)
words = reg.findall(text)
result = {}
result['l_zdan'] = len(cleared_sentences)
result['zdania'] = cleared_sentences
result['l_slow'] = len(words)
result['slowa'] = words
with open('wynik.json', 'w') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)
