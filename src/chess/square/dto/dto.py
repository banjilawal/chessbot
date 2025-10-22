from chess.coord import CoordDTO
from chess.square import Square
from chess.system import DTO, LoggingLevelRouter


class SquareDTO(DTO[Square]):
    """"""
    _id: int
    _name: str
    _coord_dto: CoordDTO

    @LoggingLevelRouter.monitor
    def __init__(self, id: int, name: str, coord_dto: CoordDTO):
        super().__init__()
        self._id = id
        self._name = name
        self._coord_dto = coord_dto
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def coord_dto(self) -> CoordDTO:
        return self._coord_dto
    
    def to_dict(self) -> dict:
        return {
            "square_id": self._id,
            "square_name": self._name,
            "coord_dto": self._coord_dto.to_dict()
        }
    
    