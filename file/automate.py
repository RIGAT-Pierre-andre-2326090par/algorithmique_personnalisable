from file.lang_repo import langs
from file.state import State


def insert(word_in: str, word: State, i: int, out: list[str]) -> None:
    if word.decalage == 1:
        out.insert(i, word.equivalent(word_in))
    else:
        out.insert(word.decalage, word.equivalent(word_in))


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
                    insert(word, self.actual, j, out[i])
                    j += 1
                if self.actual.final:
                    self.actual = self.starter
            i += 1
        return out
