from pprint import pprint
char_frequency = {}

with open('testo.txt', 'r') as tesst:
    test = tesst.read()
    for char in test:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    print(sorted(char_frequency.items(), key=lambda kv: kv[1])) 
    // comment