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


class OccupationDirective(Directive[Piece,Square]):

    def __init__(self, occupation_id: int, actor: Piece, destination_square: Square):
        super().__init__(directive_id=occupation_id, actor=actor, resource=destination_square)

    @property
    def piece(self) -> Piece:
        return self.actor

    @property
    def destination_square(self) -> Square:
        return self.resource

    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, OccupationDirective):
                return self._id == other.id
        return False

# --- AttackDirective Subclass ---
class AttackDirective(OccupationDirective):
    _attack_id: int
    _enemy: CombatantPiece
    _source_square: Square


    def __init__(
        self,
        attack_id: int,
        occupation_id: int,
        actor: Piece,
        enemy: CombatantPiece,
        source_square: Square,
        destination_square: Square
    ):
        super().__init__(occupation_id=occupation_id, actor=actor, destination_square=destination_square)
        self._enemy = enemy
        self._attack_id = attack_id
        self._source_square = source_square

    @property
    def attack_id(self) -> int:
        return self._attack_id


    @property
    def enemy(self) -> CombatantPiece:
        return self._enemy


    @property
    def source_square(self) -> Square:
        return self._source_square


    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, AttackDirective):
                return self._attack_id == other.attack_id
        return False


# --- ScanDirective Subclass ---
class ScanDirective(OccupationDirective):
    _scan_id: int
    _subject: Piece

    def __init__(
        self,
        scan_id: int,
        occupation_id: int,
        actor: Piece,
        subject: Piece,
        destination_square: Square
    ):
        super().__init__(occupation_id=occupation_id, actor=actor, destination_square=destination_square)
        self._scan_id = scan_id
        self._subject = subject

    @property
    def scan_id(self) -> int:
        return self._scan_id

    @property
    def observer(self) -> Piece:
        return self.actor

    @property
    def subject(self) -> Piece:
        return self._subject


    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, ScanDirective):
                return self._scan_id == other.scan_id
        return False