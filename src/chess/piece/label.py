class Label:
    _letters: str
    _number: int

    def __init__(self, letters: str, number: int):
        self._letters = letters
        self._number = number


    @property
    def letters(self) -> str:
        return self._letters


    @property
    def number(self) -> int:
        return self._number


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Label):
            return False
        return self._letters == other.letters and self._number == other.number


    def __hash__(self):
        return hash((self._letters, self._number))


    def __str__(self):
        return f"{self._letters}{self._number}"