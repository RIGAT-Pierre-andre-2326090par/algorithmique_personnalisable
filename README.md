# algorithmique_personnalisable

## Description

Ce projet est un compilateur en python permmettant de compiler n'importe quel langage de programmation.

## Utilisation

Pour utiliser ce projet, ouvrez le fichier `run.py` depuis un IDE ou un éditeur de texte. Ensuite, exécutez modifier les variables en fonction de vos besoins :
- `run_the_program` : booléen permettant de déterminer si le programme doit être exécuté ou compilé.
- `lang` : langage de programmation à compiler, récupérer depuis `file/lang/lang_repo.py`.
- `program` : programme à compiler/executer.

## Créer son langage

Pour créer son propre langage de programmation, il suffit d'ajouter une entrée dans le dictionnaire `langs` du fichier `file/lang_repo` et compléter le langage en respectant la forme suivante :

```python
langs: dict[str, State] = {
    "lang_name": State("\_", "\_", "Start of the program", [
        # Add your instructions pieces here
    ])
}
```

À noter que `"\_"` est le caractère représentant un caractère vide, également représenter par $\epsilon$.

Les instructions à rajouter sont de la forme :
```python
State(
    word: str, # le mot à reconnaitre
    equals: str, # son équivalent en python
    comment: str = '', # un commentaire, répond aux questions "qu'est-ce que c'est ? qu'est-ce qu'il fait ?" (non utilisé dans le programme)
    transitions: list[State] = [], # les transitions possibles, redirigent vers d'autres états
    final: bool = False, # si l'instruction est finale (indique si le compilateur doit lire la séquence suivante comme un nouveau départ (fonction, variable...))
    decalage: int = 1, # le décalage a appliqué (1 pour aucun).
    condition: tuple[tuple[int, str], str, str] = () # la condition a appliqué (de la forme "si le mot int position plus loin vaut str, alors le mot vaut str, str sinon)
)
```

Ce qui donne pour un langage qui ne peut lire que l'instruction `Afficher "Hello World!".` (qui correspond à `print("Hello World!")` en python) :
```python
 State('Afficher', 'print(', "Affichage d'élément", [
        State('\*', '\*', "L'élément à afficher", [
            State('.', ')', "Fin de l'instruction", [], True)
        ])
    ])
```

À noter ici que le caractère `\*` est un caractère générique, symbolisant un mot ou une chaine de caractère.

## À noter

Ce projet étant en cours de développement, l'implémentation de certaines notions de programmation (les boucles notament) peuvent être complex voir impossible.
