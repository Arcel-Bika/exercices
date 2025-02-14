# Résolution de l'exercice Global Tech - JavaScript - Exercice 05

## Énoncé

```javascript
let table = [1, 2, 3, 4, 5];
let result = table.fill(0);
console.log(result);
```

## Analyse du code

    Un tableau table est déclaré avec les valeurs [1, 2, 3, 4, 5].
    La méthode .fill(value) est utilisée :
        table.fill(0) remplace toutes les valeurs du tableau par 0.
        La méthode .fill() modifie le tableau en place et retourne le même tableau modifié.
    Après l'exécution, table devient [0, 0, 0, 0, 0], et result contient cette même référence.

## Réponse correcte :

C. [0, 0, 0, 0, 0]