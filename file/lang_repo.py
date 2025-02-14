from file.state import State

langs: dict[str, State] = {'fr': State('\_', '\_', 'Début du programme', [
    State('\n', '\n', "Saut de ligne", [], True),
    State('.', '\n', "Fin d'une instruction", [], True),
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
    ]),
    State('Incrémenter', '+=', "Incrémentation d'une variable", [
        State('\*', '\*', "Nom de la variable", [
            State('de', '', "", [
                State('\*', '\*', "Valeur de l'incrémentation", [
                    State('.', '', "Fin de l'instruction", [], True)
                ])
            ]),
            State('.', '1', "Fin de l'instruction", [], True)
        ])
    ], decalage=2),
    State('Décrémenter', '-=', "Décrémentation d'une variable", [
        State('\*', '\*', "Nom de la variable", [
            State('de', '', "", [
                State('\*', '\*', "Valeur de la décrémentation", [
                    State('.', '', "Fin de l'instruction", [], True)
                ])
            ]),
            State('.', '1', "Fin de l'instruction", [], True)
        ])
    ], decalage=2),
    State('Multiplier', '*=', "Multiplication d'une variable", [
        State('\*', '\*', "Nom de la variable", [
            State('par', '', "", [
                State('\*', '\*', "Valeur du multiplicateur", [
                    State('.', '', "Fin de l'instruction", [], True)
                ])
            ])
        ])
    ], decalage=2),
    State('Diviser', '/=', "Division d'une variable", [
        State('\*', '\*', "Nom de la variable", [
            State('par', '', "", [
                State('\*', '\*', "Valeur du diviseur", [
                    State('.', '', "Fin de l'instruction", [], True)
                ])
            ])
        ])
    ], decalage=2)
])}