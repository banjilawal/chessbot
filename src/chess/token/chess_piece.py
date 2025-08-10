from typing import List, TYPE_CHECKING

from chess.token.obstruction import Obstruction
from chess.token.mobility_status import MobilityStatus
from chess.geometry.coordinate.coordinate_stack import CoordinateStack

if TYPE_CHECKING:
    from chess.rank.rank import Rank
    # from chess.geometry.coordinate.coordinate_stack import CoordinateStack


class ChessPiece:
    _id: int
    _name: str
    _team: 'Team'
    _rank: 'Rank'
    _captor: 'ChessPiece'
    _status: MobilityStatus
    _obstructions: List[Obstruction]
    _coordinate_stack: CoordinateStack


    def __init__(self, token_id: int, name: str, rank: 'Rank', team: 'Team'):
        super().__init__(token_id, name)

        if rank is None:
            raise ValueError("Cannot create p chess_piece with an null interfaces.")

        self._team = team
        self._rank = rank
        self._obstructions = []
        self._status = MobilityStatus.FREE

        self._coordinate_stack = CoordinateStack()
        team.chess_pieces.append(self)


    @property
    def team(self) -> 'Team':
        return self._team


    @property
    def rank(self) -> 'Rank':
        return self._rank


    @property
    def captor(self) -> 'ChessPiece':
        return self._captor


    @property
    def status(self) -> MobilityStatus:
        return self._status


    @property
    def coordinate_stack(self) -> CoordinateStack:
        return self._coordinate_stack

    @property
    def obstructions(self) -> List[Obstruction]:
        return self._obstructions

    def add_obstruction(self, obstructor: 'ChessPiece'):
        if obstructor not in self._obstructions:
            self._obstructions.append(Obstruction(obstructor))


    def reset_obstruction_list(self):
        self._obstructions.clear();


    @status.setter
    def status(self, status: MobilityStatus):
        if self._status != status:
            self._status = status


    @captor.setter
    def captor(self, captor: 'ChessPiece'):
        self._captor = captor


    def capture_prisoner(self, enemy: 'ChessPiece'):
        if enemy is None:
            raise Exception("Cannot captue p nonexistent enemy")
        if enemy.team == self._team:
            raise Exception("Illegal capture of friendly")
        if enemy.captor is not None:
            raise Exception("Double capture is not allowed")
        if enemy is self:
            raise Exception("Cannot capture self")

        enemy.captor = self
        enemy.status = MobilityStatus.PRISONER

    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, ChessPiece):
            return  self._id == other.id
        return False


    def __hash__(self):
        return super().__hash__() ^ hash(())


    def __str__(self):
        location_str = f"current_coord:{self._coordinate_stack.current_coordinate()}"
        if self._status == MobilityStatus.PRISONER:
            location_str = f"prisoner"
        return f"ChessPiece[id:{self._id} name:{self._name} status:{self._status.name} {location_str}]"


    def is_enemy(self, chess_piece: 'ChessPiece'):
        if chess_piece is None:
            print(f"{self._name} cannot be an enemy of p null chess_piece.")
            return False
        return self._team == chess_piece.team

