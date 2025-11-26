from chess.checkmate import CheckRecord


class KingCheckRecordPosting:
    _id: int
    _record: CheckRecord
    
    def __init__(self, id: int, record: CheckRecord):
        self._id = id
        self._record = record
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def record(self) -> CheckRecord:
        return self._record
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, KingCheckRecordPosting):
            return self._id == other._id
        return False