class Row:
    _id: int

    def __int__(self, row_id: int):
        if row_id < 0:
            print("row_id cannot be negative.")
            return
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