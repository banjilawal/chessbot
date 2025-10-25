from chess.coord import Coord


class KingCheckRecord:
    _poster_id: int
    _poster_name: str
    _poster_position: Coord
    _king_id: int
    _king_name: str
    _king_position: Coord
    
    def __init__(self,
            poster_id: int,
            poster_name: str,
            poster_position: Coord,
            king_id: int,
            king_name: str,
            king_position: Coord
    ):
        self._poster_id = poster_id
        self._poster_name = poster_name
        self._poster_position = poster_position
        self._king_id = king_id
        self._king_name = king_name
        self._king_position = king_position
        
    @property
    def poster_id(self) -> int:
        return self._poster_id
    
    @property
    def poster_name(self) -> str:
        return self._poster_name
    
    @property
    def poster_position(self) -> Coord:
        return self._poster_position
    
    @property
    def king_id(self) -> int:
        return self._king_id
    
    @property
    def king_name(self) -> str:
        return self._king_name
    
    @property
    def king_position(self) -> Coord:
        return self._king_position
    
     
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, KingCheckRecord):
            return (
                (self._poster_id == other._poster_id and self._poster_position == other.poster_position) and
                (self._king_id == other._king_id and self._king_position == other.king_position)
            )
        return False
        
    def __str__(self):
        return (
            f"poster_id:{self._poster_id}, "
            f"poster_name:{self._poster_name}, "
            f"poster_position:{self._poster_position}, "
            f"king_id:{self._king_id}, "
            f"king_nam:{self._king_name}, "
            f"king_position:{self._king_position}"
        )
    
    def __repr__(self):
        return (f"<KingCheckRecord poster_id={self._poster_id} poster_name={self._poster_name} "
                f"poster_position={self._poster_position} king_id={self._king_id} king_name={self._king_name} "
                f"king_position={self._king_position}>")