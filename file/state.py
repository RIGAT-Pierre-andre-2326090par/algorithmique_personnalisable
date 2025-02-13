class State:
    def __init__(self, word: str, equals: str, comment: str = '', transitions=None, final: bool = False,
                 decalage: int = 1, condition: tuple[tuple[int, str], str, str] = ()) -> None:
        if transitions is None:
            transitions = []
        self.word: str = word
        self.comment: str = comment
        self.transitions: list[State] = transitions
        self.equals: str = equals
        self.final: bool = final
        self.decalage: int = decalage
        self.condition: tuple[tuple[int, str], str, str] = condition

    def get(self, i: int) -> list:
        out = [self]
        for j in range(i):
            for k in out:
                for l in k.transitions:
                    out.append(l)
                out.remove(k)
        return out

    def equivalent(self, word: str) -> str:
        if self.word == '\*':
            return word
        elif self.word == '\_':
            return ''
        elif self.condition != ():
            if self.is_in_next(self.condition[0][1], self.condition[0][0]):
                return self.condition[1]
            else:
                return self.condition[2]
        elif self.word == word:
            return self.equals
        else:
            return ''

    def is_in_next(self, word: str, i: int) -> bool:
        for i in self.get(i):
            if i.word == '\*' or i.word == word:
                return True
        return False

    def is_in(self, word: str) -> bool:
        for i in self.transitions:
            if i.word == '\*' or i.word == word:
                return True
        return False

    def find_next(self, word: str, i: int) -> int:
        for j in range(len(self.get(i))):
            if self.get(i)[j].word == word or self.get(i)[j].word == '\*':
                return j
        return -1

    def find(self, word: str) -> int:
        for i in range(len(self.transitions)):
            if self.transitions[i].word == word or self.transitions[i].word == '\*':
                return i
        return -1
