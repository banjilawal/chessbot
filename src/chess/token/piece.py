from typing import List, TYPE_CHECKING, Optional

from chess.token.obstruction import Obstruction
from chess.token.mobility_status import MobilityStatus
from chess.geometry.coordinate.coord_stack import CoordinateStack
from chess.token.base import Token

if TYPE_CHECKING:
    from chess.rank.rank import Rank
    # from chess.geometry.coordinate.coordinate_stack import CoordinateStack

    """"
    
    """


class ChessPiece(Token):
    _id: int
    _name: str
    _team: 'Team'
    _rank: 'Rank'
    _captor: 'ChessPiece'
    _status: MobilityStatus
    _obstructions: List[Obstruction]
    _positions: CoordinateStack


    def __init__(self, token_id: int, name: str, rank: 'Rank', team: 'Team'):
        super().__init__(token_id, name)

        if rank is None:
            raise ValueError("Cannot create p captor with an null interfaces.")

        if team is None:
            raise ValueError("Cannot create a chess piece with a null team.")

        self._team = team
        self._rank = rank
        self._obstructions = []
        self._status = MobilityStatus.FREE

        self._positions = CoordinateStack()
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
    def positions(self) -> CoordinateStack:
        return self._positions


    @property
    def obstructions(self) -> List[Obstruction]:
        return self._obstructions

    #
    #
    # def get_id(self):
    #     return self._id
    #
    #
    # def get_name(self):
    #     return self._name


    def add_obstruction(self, obstructor: 'ChessPiece'):
        if obstructor is None:
            raise Exception("Cannot add null obstruction.")
        if obstructor.status != MobilityStatus.PRISONER:
            raise Exception("A prisoner is not on the chessboard it cannot be blocking")
        if obstructor is self:
            raise Exception("Cannot block self.")

        if obstructor not in self._obstructions:
            self._obstructions.append(Obstruction(obstructor))
        print("Obstruction added")


    def reset_obstruction_list(self):
        self._obstructions.clear();


    @status.setter
    def status(self, status: MobilityStatus):
        if self._status != status:
            self._status = status


    @captor.setter
    def captor(self, captor: 'ChessPiece'):
        if captor is None:
            raise Exception("Captor cannot be null,")
        if captor.status != MobilityStatus.FREE:
            raise Exception("Captor must be free. Capture failed")
        if not self.is_enemy(captor):
            raise Exception("Captor cannot be from the same team as the piece to be captured.")
        if  captor is self:
            raise Exception("Cannot capture self.")
        if self._status != MobilityStatus.FREE:
            raise Exception("Cannot capture a piece that is already captured.")

        self._captor = captor
        self._status = MobilityStatus.PRISONER


    # def capture_prisoner(self, enemy: 'ChessPiece'):
    #     if enemy is None:
    #         raise Exception("Cannot capture p nonexistent enemy")
    #     if enemy.team == self._team:
    #         raise Exception("Illegal capture of friendly")
    #     if enemy.captor is not None:
    #         raise Exception("Double capture is not allowed")
    #     if enemy is self:
    #         raise Exception("Cannot capture self")
    #
    #     enemy.captor = self
    #     enemy.status = MobilityStatus.PRISONER

    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, ChessPiece):
            return  self._id == other.id
        return False


    def __hash__(self):
        return super().__hash__() ^ hash(())


    def __str__(self):
        return (
            f"ChessPiece[id:{self._id} "
            f"name:{self._name} "
            f"total_positions:{self._positions.size()} "
            f"current_position: {self._positions.current_coordinate} "
            f"status:{self._status.name}"
        )


    def is_enemy(self, chess_piece: 'ChessPiece'):
        if chess_piece is None:
            raise Exception("Cannot run is_enemy() check on a null captor.")
        return self._team != chess_piece.team

