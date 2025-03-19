# Résolution de l'exercice Global Tech - JavaScript - Exercice 07

## Énoncé

```javascript
const x = [5];
const y = x == false;
const z = x === false;

console.log(z);
```

## Analyse du code

    Déclaration des variables :
        x = [5] : x est un tableau contenant un seul élément 5.

    Comparaison y = x == false :
        L'opérateur == (égalité faible) effectue une coercition de type.
        En JavaScript, un tableau vide ([]) est converti en false, mais un tableau non vide ([5]) est converti en true.
        Cependant, JavaScript effectue la conversion suivante :
    [5] == false

équivaut à :
        Number([5]) == Number(false)
        5 == 0 // false

        Donc, y = false.

    Comparaison z = x === false :
        L'opérateur === (égalité stricte) ne fait aucune conversion.
        x est un tableau (object en JavaScript) et false est un booléen (boolean).
        Comme les types sont différents, la comparaison retourne false.

    Affichage de console.log(z):
        z = false, donc l'affichage est false.

## Réponse correcte :

B. false