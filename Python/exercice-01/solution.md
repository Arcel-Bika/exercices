# Résolution de l'exercice Global Tech - Python - Exercice 01

## Énoncé

```python
user: dict = {"name": "John", "age": 30, "city": ..., "email": "john@exemple.com"}

print(all(user.values()))
```

## Analyse du code

    La variable user est un dictionnaire contenant quatre clés : "name", "age", "city", et "email".
    La fonction all(iterable) retourne True si toutes les valeurs de l'itérable sont évaluées comme True en contexte booléen. Sinon, elle retourne False.
    Les valeurs du dictionnaire sont :
        "John" → True (chaîne non vide)
        30 → True (nombre différent de 0)
        ... (Ellipsis) → ⚠️ Problème potentiel
        "john@exemple.com" → True (chaîne non vide)

Comportement de Ellipsis (...) en Python

L'objet Ellipsis (...) est une valeur spéciale en Python utilisée dans certains contextes (ex : slicing, annotations de type).
Son évaluation booléenne est toujours True :

bool(...)  # Résultat : True

Évaluation de all(user.values())

Puisque toutes les valeurs sont évaluées comme True, l'expression all(user.values()) retourne :

✅ True
## Réponse correcte :

A. True
