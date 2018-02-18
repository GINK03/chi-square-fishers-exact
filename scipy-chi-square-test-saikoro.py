from scipy import stats

import random

from collections import Counter
observed = []
for i in range(1000):
  x = random.choice([x+1 for x in range(6)])
  observed.append(x)

observed = [freq for me, freq in sorted(dict(Counter(observed)).items(), key=lambda x:x[1]) ]
print(observed)

expected = [1000*1/6 for i in range(6)]
print(expected)

chisq,p = stats.chisquare(observed,expected)

print(f'chisq {chisq}')
print(f'p-val {p}')
