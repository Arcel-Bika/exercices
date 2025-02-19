"""
Global Tech - Python - Exercice 04
"""

from collections import defaultdict


d = defaultdict(str)
d["a"] += "1"
d["a"] += "2"
d["b"] += "3"

# Answer:

# A. {"a": 2, "b": [3]}
# B. {"a": ["1", "2"], "b": 3}
# C. {"a": 2, "b": 3}
# D. {"a": [1, 2], "b": [3]}
# E. {"a": "12", "b": "3"}