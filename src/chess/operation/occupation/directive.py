from typing import cast

from chess.board import Board
from chess.square import Square
from chess.operation import Directive
from chess.piece import Piece, CombatantPiece


class OccupationDirective(Directive):

    def __init__(self, directive_id: int, actor: Piece, target: Square):
        super().__init__(directive_id=directive_id, actor=actor, target=target)

    @property
    def id(self) -> int:
        return self._id

    @property
    def piece(self) -> Piece:
        return cast(Piece, self.target)

    @property
    def square(self) -> Square:
        return cast(self._target, Square)

    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, OccupationDirective):
                return self._id == other.id
        return False


class AttackDirective(OccupationDirective):
    _enemy: CombatantPiece
    _board: Board

    def __init__(self, directive_id: int, actor: Piece, target: Square, enemy: CombatantPiece, board: Board):
        super().__init__(directive_id=directive_id, actor=actor, target=target)
        self._enemy = enemy
        self._board = board


    @property
    def enemy(self) -> CombatantPiece:
        return self._enemy

    @property
    def board(self) -> Board:
        return self._board


    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, AttackDirective):
                return self._enemy == other.enemy and self._board == other.board
        return False


class ScanDirective(OccupationDirective):
    _subject: Piece

    def __init__(self, directive_id: int, actor: Piece, target: Square, subject: Piece):
        super().__init__(directive_id=directive_id, actor=actor, target=target)
        self._subject = subject

    @property
    def subject(self) -> Piece:
        return self._subject

    def __eq__(self, other):
        if not super().__eq__(other):
            if isinstance(other, ScanDirective):
                return self._subject.id == other.subject.id
        return False