# Résolution de l'exercice Global Tech - Python - Exercice 02

## Énoncé

```python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
```

## Analyse du code

    my_list est initialisée avec [1, 2, 3].
    La méthode .extend() est appelée avec [4, 5, 6] comme argument :
        .extend(iterable) ajoute chaque élément de l'itérable à la fin de la liste existante.
        Ainsi, [4, 5, 6] est décomposé et ajouté individuellement à my_list.
    Après l'exécution de my_list.extend([4, 5, 6]), la liste devient :

    [1, 2, 3, 4, 5, 6]

## Réponse correcte :

C. [1, 2, 3, 4, 5, 6]