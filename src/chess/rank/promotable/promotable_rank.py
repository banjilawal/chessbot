from typing import Optional, List

from chess.geometry.coordinate import Coordinate
from chess.geometry.quadrant import Quadrant
from chess.motion.service.motion_service import MotionService
from chess.rank.queen import Queen
from chess.rank.rank import Rank
from chess.transaction.transaction_result import TransactionResult
from chess.transaction.status_code import StatusCode
from chess.transaction.failure import Failure

class PromotableRank(Rank):
    _previous_rank: Optional[Rank] = None

    def __init__(
        self,
        name: str,
        acronym: str,
        motion_service: MotionService,
        capture_value: int,
        territories: List[Quadrant],
        previous_rank: Optional[Rank] = None
    ):
        super().__init__(name, acronym, motion_service, capture_value, territories)
        self._previous_rank = previous_rank

    def is_promoted(self) -> bool:
        return self._previous_rank is not None

    def promote(self, piece: 'Piece') -> TransactionResult:
        method = "PromotableRank.promote"

        if self.is_promoted():
            return TransactionResult(
                method_name=method,
                status=StatusCode.FAILURE,
                outcome=Failure(StatusCode.FAILURE, f"{piece.label} has already been promoted.")
            )

        previous_stack_size = len(piece.coordinate_stack)
        previous_top = piece.coordinate_stack[-1] if piece.coordinate_stack else None
        previous_id = piece.id

        new_rank = Queen(previous_rank=self)
        piece.assign_rank(new_rank)

        if self._promotion_succeeded(piece, previous_stack_size, previous_top, previous_id):
            return TransactionResult(method_name=method, status=StatusCode.SUCCESS, outcome=StatusCode.SUCCESS)

        return TransactionResult(
            method_name=method,
            status=StatusCode.FAILURE,
            outcome=Failure(StatusCode.FAILURE, f"Promotion failed integrity check on piece {piece.id}")
        )

    def _promotion_succeeded(self, piece: 'Piece', old_stack_size: int, old_top: Coordinate, old_id: int) -> bool:
        if not isinstance(piece.rank, QueenRank):
            return False
        if hasattr(piece.rank, "piece_id") and piece.rank.piece_id != old_id:
            return False
        if len(piece.coordinate_stack) != old_stack_size:
            return False
        if piece.coordinate_stack[-1] != old_top:
            return False
        return True
