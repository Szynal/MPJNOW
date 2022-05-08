with open('text.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    print(line)
with open('tekst_nieparzyste.txt', 'w') as file:
    for i, line in enumerate(lines):
        if (i + 1) % 2 == 1:
            file.write(line)
