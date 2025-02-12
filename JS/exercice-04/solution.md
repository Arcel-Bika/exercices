# Résolution de l'exercice Global Tech - JavaScript - Exercice 04

## Énoncé

```javascript
let result = ((x) => {
    return x * 3;
})(null);
```

## Analyse du code
    Une fonction fléchée immédiatement invoquée (IIFE - Immediately Invoked Function Expression) est utilisée :

(x) => { return x * 3; }

Cette fonction prend un paramètre x et retourne x * 3.

La fonction est immédiatement appelée avec null comme argument :

    ((x) => { return x * 3; })(null);

    Évaluation de null * 3 :
        En JavaScript, null est converti en 0 lors d'une multiplication.
        Donc, null * 3 = 0.

    La valeur retournée est 0 et stockée dans result.

## Réponse correcte :

D. 0