import json
import random

f = open("quotes2.json")
quotes = json.load(f)
markov = {}
quotes[0] = quotes[0].replace("lyinglying", "lying lying")
a = 0
max_len = []
n_grame = 2
next_word = ""
current_word = ""
for q in quotes:

    max_len.append(len(q))
    words = q.split(' ')
    print(words)

    for i in range(len(words) - 1 - n_grame):
        current_word = " "
        next_word = " "
        for j in range(n_grame):
            current_word += words[i + j] + " "
            next_word += words[i + j + n_grame] + " "

        current_word = current_word[:-1]
        next_word = next_word[:-1]
        print(next_word)

        if current_word not in markov:
            markov[current_word] = {}
            markov[current_word][next_word] = 1
        else:
            if next_word in markov[current_word]:
                markov[current_word][next_word] = markov[current_word][next_word] + 1

            else:
                markov[current_word][next_word] = 1

    for current in markov.keys():
        total = sum(markov[current].values())

        for state, count in markov[current].items():
            markov[current][state] = markov[current][state] / total

print(markov)
with open('markov.json', 'w') as f:
    json.dump(markov, f)
