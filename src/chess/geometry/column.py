class Column:
    _id: int
    _name: str
    def __init__(self, column_id, name:str):
        if column_id < 0:
            raise print("column_id cannot be negative.")
            return
        if name is None:
            raise print("name cannot be null.")
            return
        self._id = column_id
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
        if not isinstance(other, Column):
            return False
        return self._id == other.id