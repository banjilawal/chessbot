from abc import abstractmethod

from chess.motion.logic.reachable import Reachable
from chess.motion.search.search_pattern import SearchPattern
from chess.rank.rank import Rank


class Motion(ABC):
    _logic: Reachable
    _searchPattern: SearchPattern

   @abstractmethod
   def move(self, rank: Rank, origin: Coordinate, destination: Coordinate, board: Board) -> Optional[TurnRecord]:
        pass

    @abstractmethod
    def explore(self, rank: Rank, origin: Coordinate, board: Board) -> list[Coordinate]:
        pass