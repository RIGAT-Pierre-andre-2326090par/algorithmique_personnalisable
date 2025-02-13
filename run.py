import compile

run_the_program: bool = False  # Put True if you want to run the program, false will just compile it

lang: str = 'fr'  # Put your langage code here

program: str = '''
Afficher "Hello World!".

Soit a une variable initialisée à 5.
Afficher a.
'''  # Put your program here

if __name__ == "__main__":
    if run_the_program:
        compile.run(program, lang)
    else:
        print(compile.compile_program(program, lang))
