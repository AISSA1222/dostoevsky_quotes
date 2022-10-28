import json
import random

with open("markov.json", 'r') as model:
    markov = json.load(model)
print(markov[" above all"])


def predict(model=markov, limit=400, start=" above all"):
    current = start
    next = None
    quote = ''
    n = 0
    quote = quote + current + " "
    while n < limit and current in markov:
        next = random.choices(list(markov[current].keys()), list(markov[current].values()))

        current = next[0]
        quote = quote + current + " "
        n += 1

    return quote


for i in range(10):
    print(str(i) + '-' + predict(markov, 50, ' a man'))
