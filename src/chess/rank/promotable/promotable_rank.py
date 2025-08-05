# promotable_rank.py
from typing import Optional, List, TYPE_CHECKING

from chess.geometry.quadrant import Quadrant
from chess.motion.service.motion_service import MotionService

if TYPE_CHECKING:
    from chess.piece.piece import ChessPiece
    from chess.rank.rank import Rank

class PromotableRank:
    _previous_rank: Optional['Rank'] = None

    def __init__(
        self,
        name: str,
        acronym: str,
        motion_service: MotionService,
        capture_value: int,
        territories: List[Quadrant],
        previous_rank: Optional['Rank'] = None
    ):
        from chess.rank.rank import Rank  # LOCAL IMPORT TO BREAK CYCLE
        self._previous_rank = previous_rank
        Rank.__init__(self, name, acronym, motion_service, capture_value, territories)

    def is_promoted(self) -> bool:
        return self._previous_rank is not None

    def promote(self, piece: 'ChessPiece') -> 'ChessPiece':
        pass

        # method = "PromotableRank.promote"
        #
        # if self.is_promoted():
        #     print( f"{piece.name} has already been promoted.")
        #     return piece
        # return ChessPiece(
        #     chess_piece_id = self._id
        #     rank = Queen()
        #
        #
        # )
        # #
        # previous_stack_size = len(piece.coordinate_stack)
        # previous_top = piece.coordinate_stack[-1] if piece.coordinate_stack else None
        # previous_id = piece.id
        #
        # new_rank = Queen()
        # piece.assign_rank(new_rank)


    #
    # def _promotion_succeeded(
    #         self, piece: 'ChessPiece',
    #         old_stack_size: int,
    #         old_top_coordinate: Coordinate,
    #         old_id: int
    # ) -> bool:
    #     if not isinstance(piece.rank, Queen):
    #         return False
    #     if hasattr(piece.rank, "chess_piece_id") and piece.rank.chess_piece_id != old_id:
    #         return False
    #     if len(piece.coordinate_stack) != old_stack_size:
    #         return False
    #     if piece.coordinate_stack[-1] != old_top_coordinate:
    #         return False
    #     return True
