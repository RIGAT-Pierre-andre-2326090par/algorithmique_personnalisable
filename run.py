import compile

run_the_program: bool = False  # Put True if you want to run the program, false will just compile it

lang: str = 'fr'  # Put your langage code here

program: str = '''
// Cette ligne est un commentaire, elle ne sera pas interprétée.
// Ce programme est un programme de test pour le langage de programmation "fr".
// Il est utilisé pour tester le bon fonctionnement de l'interpréteur.
// Vous pouvez jeter un œil au lignes suivantes pour comprendre le fonctionnement et la syntaxe du langage.

Afficher "Hello World!".

Soit a une variable initialisée à 5.
Afficher a.

Incrémenter a de 5.
Afficher a.

Incrémenter a.
Afficher a.

Décrémenter a de 5.
Afficher a.

Décrémenter a.
Afficher a.

Multiplier a par 5.
Afficher a.

Diviser a par 5.
Afficher a.
'''  # Put your program here

if __name__ == "__main__":
    if run_the_program:
        compile.run(program, lang)
    else:
        print(compile.compile_program(program, lang))
