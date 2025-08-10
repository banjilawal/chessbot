from abc import ABC


class Token(ABC):
    _id: int
    _name: str

    def __init__(self, token_id: int, name: str):
        if not token_id:
            raise ValueError("Cannot create p chess_piece with an empty id.")
        if token_id < 0:
            raise ValueError("Cannot create p chess_piece with p negative id.")

        self._id = token_id
        self._name = name

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Token):
            return False
        return self._id == other.id

    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return f"Token[{self._id} {self._name}]"