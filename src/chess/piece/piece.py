

from chess.geometry.coordinate import Coordinate
from chess.piece.captivity_status import CaptivityStatus
from chess.piece.label import Label



from abc import ABC
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from chess.player.player import Player
    from chess.rank.rank import Rank
    from chess.game.record.turn_record import TurnRecord
    from chess.geometry.board import Board

class Piece:
    _id: int
    _label: Label
    _rank: 'Rank'
    _player: 'Player'
    _position_history: List[Coordinate]
    _status: CaptivityStatus

    def __init__(self, piece_id: int, rank: 'Rank'):
        if not piece_id:
            raise ValueError("Cannot create a piece with an empty id.")
        if piece_id < 0:
            raise ValueError("Cannot create a piece with a negative id.")
        if rank is None:
            raise ValueError("Cannot create a piece with an null rank.")

        rank.members.append(self)
        self._rank = rank
        self._label = Label(rank.acronym, len(rank.members))

        self._id = piece_id
        self._player = None
        self._status = CaptivityStatus.FREE
        self._position_history: List[Coordinate] = []


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
        return self._position_history

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
            self.__rebuild_label()

        if old_player is not None:
            old_player.pieces.remove(self)

    def forward_move_request(self, board: 'Board', destination: Coordinate):
        if self._rank is None:
            raise ValueError("Piece has no rank assigned")
        if destination is None:
            raise ValueError("destination cannot be null.")
        self._rank.delegate_move_excution(piece=self, board=board, destination=destination)


    def explore_destinations(self, board: 'Board') -> List[Coordinate]:
        if self._rank is None:
            raise ValueError(f"Piece {self.label} has no rank assigned. It cannot explore.")
            return []
        if board is None:
            raise ValueError(f"board cannot be null. {self._label} cannot explore.")
        print(f"Everything is fine with {self._label} calling Rank.explore for the list")
        return self._rank.explore(self, board)


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Piece):
            return False
        if isinstance(other, Piece):
            self.id == other.id and self.rank == other.rank
        return False


    def __hash__(self):
        return hash((self.id, self.rank))

    def __str__(self):
        return f"{self.id} {self.label} {self.status.name} stack_size:{len(self._position_history)}"

    def is_enemy(self, piece: 'Piece'):
        return self._player == piece.player

    def __rebuild_label(self):
        old_label = self._label

        if self._player is not None:

            letters = self._player.color.name[0] + self._label.letters
            number = self._label.number % 2 + 1
            self._label = Label(letters, number)


    # === Stack operations ===
    def add_position(self, coordinate: Coordinate):
        if coordinate is None:
            raise ValueError("coord cannot be null.")
        print("current position history")
        for c in self._position_history:
            print(c)
        if coordinate in self._position_history:
            raise ValueError(f"Cannot add {coordinate} to {self._label} stack. It is already present.")
        self._position_history.append(coordinate)


    def undo_last_position(self) -> Optional[Coordinate]:
        if self._position_history:
            return self._position_history.pop()
        return None


    def current_position(self) -> Optional[Coordinate]:
        return self._position_history[-1] if self._position_history else None