from pprint import pprint
char_frequency = {}
test = open('testo.txt').read()
for char in test:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(sorted(char_frequency.items(), key=lambda kv: kv[1]))