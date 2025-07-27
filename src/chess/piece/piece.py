from enum import Enum, auto

from chess.geometry.coordinate import Coordinate
from chess.piece.captivity_status import CaptivityStatus
from chess.piece.label import Label



from abc import ABC
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from chess.player.player import Player
    from chess.rank.rank import Rank


class Piece:
    _id: int
    _label: Label
    _rank: 'Rank'
    _player: 'Player'
    _position_history: List[Coordinate]
    _status: CaptivityStatus

    def __init__(self, piece_id: int, rank: 'Rank', player: Optional['Player']=None):
        if not piece_id:
            raise ValueError("Cannot create a piece with an empty id.")
        # if not player:
        #     raise ValueError("Cannot create a piece with an null player.")
        if rank is None:
            raise ValueError("Cannot create a piece with an null rank.")
        self._id = piece_id
        self._rank = rank
        self._player = player
        self._status = CaptivityStatus.FREE
        self._position_history: List[Coordinate] = []
        self._label = None

        # if self not in player.pieces:
        #     player.pieces.append(self)
        print("size", len(rank.members))
        if rank.members is None:
            rank.members = []
        if self not in rank.members:
            rank.members.append(self)
            print("after size", len(rank.members))
        self._rank = rank


    # === Immutable attributes ===
    @property
    def id(self) -> int:
        return self._id

    @property
    def label(self) -> Label:
        return self._label


    @property
    def player(self) -> 'Player':
        return self._player


    @property
    def rank(self) -> 'Rank':
        return self._rank

    @property
    def status(self) -> CaptivityStatus:
        return self._status

    @property
    def position_history(self) -> List[Coordinate]:
        return self._position_history.copy()

    @status.setter
    def status(self, status: CaptivityStatus):
        if self._status != status:
            self._status = status

    @player.setter
    def player(self, player: 'Player'):
        if self._player == player:
            print("player is already set to", player.name)
            return
        old_player = self._player

        if player is not None:
            if player.pieces is None:
                player.pieces = []
            if not self in player.pieces:
                player.pieces.append(self)
            self._player = player

        if old_player is not None:
            old_player.pieces.remove(self)


    def is_enemy(self, piece: 'Piece'):
        return self._player == piece.player

    # === Stack operations ===
    def add_position(self, coordinate: Coordinate) -> None:
        if coordinate is None:
            raise ValueError("coordinate cannot be null.")
        self._position_history.append(coordinate)

    def undo_last_position(self) -> Optional[Coordinate]:
        if self._position_history:
            return self._position_history.pop()
        return None

    def current_position(self) -> Optional[Coordinate]:
        return self._position_history[-1] if self._position_history else None


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Piece):
            return False
        if isinstance(other, Piece):
            self.id == other.id
        return False