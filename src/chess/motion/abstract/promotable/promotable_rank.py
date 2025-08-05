# promotable_rank.py
from typing import Optional, List, TYPE_CHECKING

from chess.geometry.line.quadrant import Quadrant
from chess.motion.abstract.motion_service import MotionService

if TYPE_CHECKING:
    from chess.team.model.piece import ChessPiece
    from chess.motion.abstract.motion_controller import MotionController

class PromotableRank:
    _previous_rank: Optional['MotionController'] = None

    def __init__(
        self,
        name: str,
        acronym: str,
        motion_service: MotionService,
        capture_value: int,
        territories: List[Quadrant],
        previous_rank: Optional['MotionController'] = None
    ):
        from chess.motion.abstract.motion_controller import MotionController  # LOCAL IMPORT TO BREAK CYCLE
        self._previous_rank = previous_rank
        MotionController.__init__(self, name, acronym, motion_service, capture_value, territories)

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
        #     abstract = Queen()
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
    #     if not isinstance(piece.abstract, Queen):
    #         return False
    #     if hasattr(piece.abstract, "chess_piece_id") and piece.abstract.chess_piece_id != old_id:
    #         return False
    #     if len(piece.coordinate_stack) != old_stack_size:
    #         return False
    #     if piece.coordinate_stack[-1] != old_top_coordinate:
    #         return False
    #     return True
