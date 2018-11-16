#!/usr/bin/env python
from collections import Counter

with open('DATA/words.txt') as words_in:
    word_counts = Counter(w[0] for w in words_in)

print(word_counts)
print(word_counts['t'])

print(word_counts.most_common(5))

print(word_counts.most_common(5))
print(isinstance(word_counts, Counter))
print(isinstance(word_counts, dict))

