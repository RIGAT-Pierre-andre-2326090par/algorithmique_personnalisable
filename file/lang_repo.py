from file.state import State

langs: dict[str, State] = {'fr': State('\_', '\_', 'Début du programme', [
    State('\n', '\n', "Saut de ligne", [], True),
    State('.', '\n', "Fin d'une instruction", [], True),
    # State('//', '#', "Commentaire", []),
    State('Afficher', 'print(', "Affichage d'élément", [
        State('\*', '\*', "L'élément à afficher", [
            State('.', ')', "Fin de l'instruction", [], True)
        ])
    ]),
    State('Soit', '', "Déclaration de variable", [
        State('\*', '\*', "Nom de la variable", [
            State('une', '', "", [
                State('variable', '', "", [
                    State('initialisée', '=', "", [
                        State('à', '', "", [
                            State('\*', '\*', "Valeur de la variable", [
                                State('.', '', "Fin de la déclaration", [], True)
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])
])}