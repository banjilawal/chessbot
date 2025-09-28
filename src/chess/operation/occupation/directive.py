from typing import cast

from chess.board import Board
from chess.square import Square
from chess.operation import Directive
from chess.piece import Piece, CombatantPiece

__all__ = [
    'OccupationDirective',
    'AttackDirective',
    'ScanDirective'
]


class OccupationDirective(Directive):

    def __init__(self, occupation_id: int, actor: Piece, target_square: Square):
        super().__init__(directive_id=occupation_id, actor=actor, resource=target_square)

    @property
    def id(self) -> int:
        return self._id

    @property
    def piece(self) -> Piece:
        return cast(Piece, self.actor)

    @property
    def square(self) -> Square:
        return cast(Square, self.resource)

    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, OccupationDirective):
                return self._id == other.id
        return False

# --- AttackDirective Subclass ---
class AttackDirective(OccupationDirective):
    _enemy: CombatantPiece
    _board: Board
    _attack_id: int

    def __init__(
        self,
        occupation_id: int,
        actor: Piece,
        enemy: CombatantPiece,
        target_square: Square,
        board: Board,
        attack_id: int
    ):
        super().__init__(occupation_id=occupation_id, actor=actor, target_square=target_sqaure)
        self._enemy = enemy
        self._board = board
        self._attack_id = attack_id

    @property
    def enemy(self) -> CombatantPiece:
        return self._enemy

    @property
    def board(self) -> Board:
        return self._board

    @property
    def attack_id(self) -> int:
        return self._attack_id

    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, AttackDirective):
                return (
                    self._attack_id == other.attack_id and
                    self._enemy == other.enemy and
                    self._board == other.board
                )
        return False


# --- ScanDirective Subclass ---
class ScanDirective(OccupationDirective):
    _subject: Piece
    _scan_id: int

    def __init__(self, occupation_id: int, actor: Piece, target_square: Square, subject: Piece, scan_id: int):
        super().__init__(occupation_id=occupation_id, actor=actor, target_sqaure=target_sqaure)
        self._subject = subject
        self._scan_id = scan_id

    @property
    def subject(self) -> Piece:
        return self._subject

    @property
    def scan_id(self) -> int:
        return self._scan_id

    def __eq__(self, other):
        if not super().__eq__(other):
            if isinstance(other, ScanDirective):
                return (self._scan_id == other.scan_id and
                        self._subject.id == other.subject.id
                        )
        return False