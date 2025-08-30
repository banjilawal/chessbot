from typing import Optional, List, TYPE_CHECKING

from chess.geometry.quadrant import Quadrant
from chess.rank.queen import QueenRank
from chess.rank.base import Rank
from chess.walk.base import Walk

if TYPE_CHECKING:
    from chess.token.model import Piece


class PromotableRank(Rank):
    _previous_rank: Optional[Rank]

    def __init__(
        self,
        name: str,
        letter: str,
        capture_value:

        int, number_per_team: int,
        territories: List[Quadrant],
        walk:Optional[Walk] = None,
    ):
        super().__init__(
            name=name,
            letter=letter,
            walk=walk,
            capture_value=capture_value,
            number_per_team=number_per_team,
            territories=territories
        )
        _previous_rank = None

    @property
    def previous_rank(self) -> Optional[Rank]:
        return self._previous_rank

    def promote(self, chess_piece: 'Piece') -> Optional['Piece']:

        enemy_back_row_index = chess_piece.team.enemy_back_row_index()
        if chess_piece.positions.current_coordinate().row != enemy_back_row_index():
            print(f"{chess_piece.get_name()} is not the enemy's home row. Cannot be promoted.")
            raise TypeError(f"{chess_piece.get_name()} is not on the enemy home row. Cannot be promoted.")

        # if isinstance(self.rank, QueenRank) and self._previous_rank is not None:
        #     raise TypeError(f"{captor.name} is already promoted.")

        promoted_chess_piece = Piece(
            token_id=chess_piece.get_id(),
            name=chess_piece.get_name(),
            rank=QueenRank(),
            team=chess_piece.team
        )
        stack = chess_piece.positions.stack
        while (len(stack)) > 0:
            entry = stack.pop()
            promoted_chess_piece.positions.push_coordinate(entry)

        return promoted_chess_piece



        # method = "PromotableRank.promote"
        #
        # if self.is_promoted():
        #     print( f"{captor.name} has already been promoted.")
        #     return captor
        # return ChessPiece(
        #     chess_piece_id = self._id
        #     interfaces = Queen()
        #
        #
        # )
        # #
        # previous_stack_size = len(captor.coordinate_stack)
        # previous_top = captor.coordinate_stack[-1] if captor.coordinate_stack else None
        # previous_id = captor.id
        #
        # new_rank = Queen()
        # captor.assign_rank(new_rank)


    #
    # def _promotion_succeeded(
    #         self, captor: 'ChessPiece',
    #         old_stack_size: int,
    #         old_top_coordinate: Coordinate,
    #         old_id: int
    # ) -> bool:
    #     if not isinstance(captor.interfaces, Queen):
    #         return False
    #     if hasattr(captor.interfaces, "chess_piece_id") and captor.interfaces.chess_piece_id != old_id:
    #         return False
    #     if len(captor.coordinate_stack) != old_stack_size:
    #         return False
    #     if captor.coordinate_stack[-1] != old_top_coordinate:
    #         return False
    #     return True
