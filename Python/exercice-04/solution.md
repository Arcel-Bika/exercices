# Résolution de l'exercice Global Tech - Python - Exercice 04

## Énoncé

```python
from collections import defaultdict

d = defaultdict(str)
d["a"] += "1"
d["a"] += "2"
d["b"] += "3"
```

## Analyse du code

Création du defaultdict :

d = defaultdict(str)

    defaultdict(str) signifie que toute clé absente retournera par défaut une chaîne vide ("").

Ajout des valeurs :

d["a"] += "1"  # d["a"] = "" + "1" → "1"
d["a"] += "2"  # d["a"] = "1" + "2" → "12"
d["b"] += "3"  # d["b"] = "" + "3" → "3"

Contenu final du dictionnaire :

    d = {"a": "12", "b": "3"}

## Réponse correcte :

E. {"a": "12", "b": "3"}