# Résolution de l'exercice Global Tech - Python - Exercice 03

## Énoncé

```python
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
```

## Analyse du code

    Utilisation de defaultdict :
        defaultdict(list) crée un dictionnaire où chaque clé a automatiquement une liste vide comme valeur par défaut.
        Cela signifie que si on accède à d[key] sans l’avoir défini auparavant, une liste vide est créée automatiquement.

    Ajout d'éléments :
        d['a'].append(1): Ajoute 1 à la liste associée à la clé 'a'.
        d['a'].append(2): Ajoute 2 à la liste associée à la clé 'a'.
        d['b'].append(3): Ajoute 3 à la liste associée à la clé 'b'.

    Valeur finale de d :

    {'a': [1, 2], 'b': [3]}

## Réponse correcte :

D. {'a': [1, 2], 'b': [3]}