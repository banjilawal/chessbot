from typing import List, Sequence

from chess.exception.stack_exception import PushingNullEntityException, CorruptedStackException
from chess.piece.piece import Piece


class TeamRoster:
    _items: List[Piece]
    
    def __init__(self):
        self._items = []

    @property
    def items(self) -> Sequence[Piece]:
        """
        Returns a read-only view of the stack's contents. The returned sequence is safe to
        iterate and index, but mutating it will not affect the original stack.
        """

        return self._items.copy()


    def is_empty(self) -> bool:
        return len(self._items) == 0


    def size(self) -> int:
        return len(self._items)


    def push_piece(self, piece):
        method = "PieceStack.push"

        if piece is None:
            raise PushingNullEntityException(
                f"{method}: {PushingNullEntityException.DEFAULT_MESSAGE}"
            )

        if self._items is None:
            raise CorruptedStackException(f"{method}: {CorruptedStackException.DEFAULT_MESSAGE}")
