from bs4 import BeautifulSoup
import requests
import re
import json

url_root = "https://www.goodreads.com/author/quotes/3137322.Fyodor_Dostoevsky?page="

url1 = "https://www.goodreads.com/work/quotes/55694028-fyodor-dostoyevsky-the-complete-novels-centaur-classics?page=2"
url2 = "https://www.goodreads.com/work/quotes/55694028-fyodor-dostoyevsky-the-complete-novels-centaur-classics?page=01"
sites = [url1, url2]

for i in range(3, 100):
    url = url_root + str(i)
    sites.append(url)

all_quotes = []
for s in sites:
    r = requests.get(s)
    b = BeautifulSoup(r.text, "html.parser")

    txt = b.find_all(class_='quoteText')
    for i in range(len(txt)):
        m = txt[i].getText().split('-')
        all_quotes.append(m[0].split('\n')[1])

print(all_quotes[1])

clean = []
for q in all_quotes:
    q = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", q)
    q = q.lstrip()
    q = q.rstrip()
    q = q.lower()
    clean.append(q)

print(clean)

with open('quotes2.json', 'w') as f:
    json.dump(clean, f)
