class Row:
    _id: int


    def __init__(self, row_id: int):
        if row_id < 0:
            raise ValueError("row_id cannot be negative.")
        self._id = row_id


    @property
    def id(self) -> int:
        return self._id


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Row):
            return False
        return self._id == other.id


    def __hash__(self):
        return hash(self._id)


    def __str__(self):
        return f"{self._id}"