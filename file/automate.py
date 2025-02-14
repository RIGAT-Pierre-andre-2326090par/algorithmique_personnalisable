from file.lang_repo import langs
from file.state import State

def insert(word_in: str, word: State, i: int, out: list[str]) -> int:
    double_insert = True
    if word.decalage == 1:
        if i >= len(out):
            double_insert = False
            while i >= len(out):
                out.append('')
        elif i < 0:
            double_insert = False
            while i < 0:
                out.insert(0, '')
                i += 1
        if out[i] == '':
            out[i] = word.equivalent(word_in)
            if double_insert:
                return 2
            return 1
        else:
            out.insert(i, word.equivalent(word_in))
            return 0
    else:
        if 0 >= word.decalage >= -1:
            i = word.decalage
        elif word.decalage > 1:
            i += word.decalage - 1
        if i >= len(out):
            while i >= len(out):
                out.append('')
        if out[i] == '':
            out[i] = word.equivalent(word_in)
            return 0
        else:
            out.insert(i, word.equivalent(word_in))
            return 0


class Automate:
    def __init__(self, lang: str):
        self.starter = langs[lang]
        self.actual = self.starter

    def run(self, program: list[list[str]]) -> list[list[str]]:
        out: list[list[str]] = []
        i: int = 0
        for line in program:
            out.append([])
            j: int = 0
            for word in line:
                if self.actual.is_in(word):
                    self.actual = self.actual.transitions[self.actual.find(word)]
                    j += insert(word, self.actual, j, out[i])
                elif self.actual == self.starter and word != '':
                    break
                if self.actual.final:
                    self.actual = self.starter
            i += 1
        return out
