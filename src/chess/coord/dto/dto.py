from chess.system import DTO, Result
from chess.coord import Coord, CoordValidator


class CoordDTO(DTO[Coord]):
    _row: int
    _column: int
    
    def init(self, row: int, column: int):
        self._row = row
        self._column = column
    
    @property
    def row(self) -> int:
        return self._row
    
    @property
    def column(self) -> int:
        return self._column
    
    def __init__(self, row: int, column: int):
        method = "CoordDTO.__init__"
        self._row = row
        self._column = column
    
    def to_dict(self) -> dict:
        return {"row": self._row, "column": self._column}
    
    @classmethod
    def convert(cls, candidate: Coord) -> Result[DTO[Coord]]:
        method = "CoordDTO.convert"
        try:
            validation = CoordValidator.validate(candidate)
            if not validation.is_failure():
                return Result(exception=validation.exception)
            return Result(payload=CoordDTO(row=candidate.row, column=candidate.column))
        except Exception as e:
            return Result(exception=e)
    


    
