import numpy as np
from collections import defaultdict
import urllib.request
import tempfile

url = 'https://raw.githubusercontent.com/dwyl/english-words/master/' \
      'words_alpha.txt'

with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as tmp:
    urllib.request.urlretrieve(url, tmp.name)

    print('reading vocabulary')
    words = []
    struct = defaultdict(list)
    with open(tmp.name, 'r') as f:
        while True:
            w = f.readline().rstrip('\n')
            if not w:
                break
            if len(w) >= 4:
                ul = np.unique([l for l in w])
                for l in ul:
                    struct[l].append(w)
print('done')

mandatory = 's'
optional = {'t', 'e', 'c', 'a', 'o', 'r'}
alphabet = optional.union(mandatory)
print(f'mandatory: {mandatory}')
print(f'optional: {optional}')
print(f'alphabet: {alphabet}')

print('Admissible words:')
count = 0
for w in struct[mandatory]:
    if set([l for l in w]).issubset(alphabet):
        count += 1
        print(count, w)
