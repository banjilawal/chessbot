from typing import Optional, List, TYPE_CHECKING

from chess.geometry.quadrant import Quadrant
from chess.rank.queen_rank import QueenRank
from chess.motion.walk.walk import Walk

if TYPE_CHECKING:
    from chess.team.model.piece import ChessPiece


class PromotableRank:

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:
        int, number_per_team: int,
        territories: List[Quadrant],
        walk:Optional[Walk] = None,
        # explorer:Optional[Explorer] = None,
    ):
        super().__init__(
            name=name,
            letter=letter,
            walk=walk,
            # explorer=explorer,
            capture_value=capture_value,
            number_per_team=number_per_team,
            territories=territories
        )


    def promote(self, chess_piece: 'ChessPiece') -> Optional['ChessPiece']:

        enemy_back_row_index = chess_piece.team.enemy_back_row_index()
        if chess_piece.coordinate_stack.current_coordinate().row != enemy_back_row_index():
            print(f"{chess_piece.name} is not the enemy's home row. Cannot be promoted.")
            raise TypeError(f"{chess_piece.name} is not on the enemy home row. Cannot be promoted.")

        if isinstance(self.rank, QueenRank) and self._previous_rank is not None:
            raise TypeError(f"{chess_piece.name} is already promoted.")

        promoted_chess_piece = ChessPiece(
            chess_piece_id=chess_piece.id,
            name=chess_piece.name,
            motion_controller=QueenRank(),
            team=chess_piece.team
        )
        stack = chess_piece.coordinate_stack.stack
        while (len(stack)) > 0:
            entry = stack.pop()
            promoted_chess_piece.coordinate_stack.push_coordinate(entry)

        return promoted_chess_piece



        # method = "PromotableRank.promote"
        #
        # if self.is_promoted():
        #     print( f"{chess_piece.name} has already been promoted.")
        #     return chess_piece
        # return ChessPiece(
        #     chess_piece_id = self._id
        #     interfaces = Queen()
        #
        #
        # )
        # #
        # previous_stack_size = len(chess_piece.coordinate_stack)
        # previous_top = chess_piece.coordinate_stack[-1] if chess_piece.coordinate_stack else None
        # previous_id = chess_piece.id
        #
        # new_rank = Queen()
        # chess_piece.assign_rank(new_rank)


    #
    # def _promotion_succeeded(
    #         self, chess_piece: 'ChessPiece',
    #         old_stack_size: int,
    #         old_top_coordinate: Coordinate,
    #         old_id: int
    # ) -> bool:
    #     if not isinstance(chess_piece.interfaces, Queen):
    #         return False
    #     if hasattr(chess_piece.interfaces, "chess_piece_id") and chess_piece.interfaces.chess_piece_id != old_id:
    #         return False
    #     if len(chess_piece.coordinate_stack) != old_stack_size:
    #         return False
    #     if chess_piece.coordinate_stack[-1] != old_top_coordinate:
    #         return False
    #     return True
