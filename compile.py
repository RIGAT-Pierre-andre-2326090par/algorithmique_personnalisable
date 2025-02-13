from file.automate import Automate


def split_by_line(program: str) -> list[str]:
    out = []
    tmp = ''
    for c in program:
        tmp += c
        if c == '\n':
            out.append(tmp)
            tmp = ''
    out.append(tmp)
    return out


def split_by_space(program: str) -> list[str]:
    out = []
    tmp = ''
    tmp2 = ''
    is_2 = False
    for c in program:
        if c in '"\'' and not is_2:
            is_2 = True
            tmp2 = ''
            tmp2 += c
        elif is_2:
            tmp2 += c
            if c in '"\'':
                is_2 = False
                out.append(tmp2)
        elif c in ' .:;()[]{}\n':
            out.append(tmp)
            if c != ' ':
                out.append(c)
            tmp = ''

        else:
            tmp += c
    out.append(tmp)
    return out


def split_program(program: str) -> list[list[str]]:
    out = []
    program = split_by_line(program)
    for line in program:
        line = split_by_space(line)
        out.append(line)
    return out


def join_by_space(program: list[str]) -> str:
    out = ''
    for word in program:
        out += word # + ' '
    if out != '':
        while len(out) > 1:
            if out[0] == '\n' or out[0] == ' ':
                out = out[1:]
            else:
                break
    return out


def join_by_line(program: list[str]) -> str:
    out = ''
    for line in program:
        out += line
    return out


def join_program(program: list[list[str]]) -> str:
    out = []
    for line in program:
        line = join_by_space(line)
        out.append(line)
    out = join_by_line(out)
    return out


def compile_program(program: str, lang: str) -> str:
    program = split_program(program)
    program = Automate(lang).run(program)
    program = join_program(program)
    return program


def run(program: str, lang: str):
    program = compile_program(program, lang)
    program = str(program)
    exec(program)
