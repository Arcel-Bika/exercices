"""
Global Tech - Python - Exercice 03
"""

from collections import defaultdict


d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)


# Answer:
# A. {'a': 2, 'b': [3]} 
# B. {'a': [1, 2], 'b': 3}
# C. {'a': 2, 'b': 3}
# D. {'a': [1, 2], 'b': [3]}
