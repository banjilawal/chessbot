

from chess.square import Square, SquareValidator
from chess.system import DTO, LoggingLevelRouter, Result


class SquareDTO(DTO[Square]):
    _id: int
    _name: str
    _coord_dto: CoordDTO

    def __init__(self, id: int, name: str, coord_dto: CoordDTO):
        super().__init__()
        self._id = id
        self._name = name
        self._coord_dto = coord_dto
    
    @classmethod
    @LoggingLevelRouter.monitor
    def convert(cls, candidate: Square) -> Result[DTO[Square]]:
        validation = SquareValidator.validate(candidate)
        if validation.is_failure():
          return Result(exception=validation.exception)
        
        cls._square_id = candidate.id
        cls._name = candidate.name
        cls._coord_dto = CoordDTO.convert(candidate.coord)
        
        return cls