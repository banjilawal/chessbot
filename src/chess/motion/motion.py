from abc import ABC, abstractmethod
from typing import Optional, List, TYPE_CHECKING

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.game.record.turn_record import TurnRecord
from chess.motion.logic.reachable import Reachable
from chess.motion.search.search_pattern import SearchPattern

if TYPE_CHECKING:
    from chess.rank.rank import Rank


class Motion(ABC):
    _logic: Reachable
    _search_pattern: SearchPattern

    def __init__(self, logic: Reachable, search_pattern: SearchPattern):
        if logic is None:
            raise ValueError("Motion logic cannot be None.")
        if search_pattern is None:
            raise ValueError("Search pattern cannot be None.")

        self._logic = logic
        self._search_pattern = search_pattern

    @property
    def logic(self) -> Reachable:
        return self._logic

    @property
    def search_pattern(self) -> SearchPattern:
        return self._search_pattern

    # Final method — performs common validation before deferring to subclass logic
    def move(
        self,
        rank: 'Rank',
        origin: Coordinate,
        destination: Coordinate,
        board: Board
    ) -> Optional[TurnRecord]:
        self._validate(rank, origin, board)
        self._validate_destination(destination, board)
        return self._perform_move(rank, origin, destination, board)

    # Final method — performs common validation before deferring to subclass logic
    def explore(
        self,
        rank: 'Rank',
        origin: Coordinate,
        board: Board
    ) -> List[Coordinate]:
        self._validate(rank, origin, board)
        return self._perform_exploration(rank, origin, board)

    @abstractmethod
    def _perform_move(
        self,
        rank: 'Rank',
        origin: Coordinate,
        destination: Coordinate,
        board: Board
    ) -> Optional[TurnRecord]:
        raise NotImplementedError("Subclasses must implement _perform_move.")

    @abstractmethod
    def _perform_exploration(
        self,
        rank: 'Rank',
        origin: Coordinate,
        board: Board
    ) -> List[Coordinate]:
        raise NotImplementedError("Subclasses must implement _perform_explore.")

    def _validate(self, rank: 'Rank', origin: Coordinate, board: Board):
        if rank is None:
            raise ValueError("Rank cannot be None.")
        if board is None:
            raise ValueError("Board cannot be None.")
        if not board.coordinate_is_valid(origin):
            raise ValueError(f"Origin coordinate {origin} is invalid.")

    def _validate_destination(self, destination: Coordinate, board: Board):
        if not board.coordinate_is_valid(destination):
            raise ValueError(f"Destination coordinate {destination} is invalid.")
