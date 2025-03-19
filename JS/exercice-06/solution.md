# Résolution de l'exercice Global Tech - JavaScript - Exercice 06

## Énoncé

```javascript
let numbers = [1, 2, 3, 4, 5];
let result = numbers.filter(num => num > 3);
```

## Analyse du code

    numbers est un tableau contenant [1, 2, 3, 4, 5].
    La méthode .filter(callback) est utilisée :
        .filter(num => num > 3) retourne un nouveau tableau contenant uniquement les éléments pour lesquels la condition num > 3 est vraie.
        Cela signifie que seuls les nombres strictement supérieurs à 3 seront inclus.
    Les nombres filtrés sont [4, 5], donc result est [4, 5].

## Réponse correcte :

A. [4, 5]