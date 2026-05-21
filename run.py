import argparse
import os

import compile

default_path: str = './program'

parser = argparse.ArgumentParser(description="A interpreter for any custom programming language to Python.")

parser.add_argument("-p", "--path", type=str, default=default_path,
                    help="Path of the program or a folder where the program is to be interpreted.")

parser.add_argument("-r", "--run_the_program", help="Run or print the interpreted program.")

args = parser.parse_args()

program: str = ""

if os.path.isdir(args.path):
    file_names = [f for f in os.listdir(args.path) if os.path.isfile(os.path.join(args.path, f))]
    if len(file_names) == 1:
        program = args.path + "/" + file_names[0]
    else:
        print("Choose a file [0-" + str(len(file_names) - 1) + "]:")
        for i in range(len(file_names)):
            print(str(i) + ". " + file_names[i])
        program = args.path + "/" + file_names[int(input("Your choice: "))]
else:
    program = args.path

name, ext = os.path.splitext(program)

lang = ext[1:]

with open(program) as f:
    program = f.read()

if args.run_the_program:
    compile.run(program, lang)
else:
    print(compile.compile_program(program, lang))
