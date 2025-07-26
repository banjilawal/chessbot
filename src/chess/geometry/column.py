class Column:
    _id: int
    _letter: str
    def __init__(self, column_id, letter:str):
        if column_id < 0:
            raise print("column_id cannot be negative.")
            return
        if letter is None:
            raise print("letter cannot be null.")
            return
        self._id = column_id
        self._letter = letter


    @property
    def id(self) -> int:
        return self._id


    @property
    def letter(self) -> str:
        return self._letter


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Column):
            return False
        return self._id == other.id