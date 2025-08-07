from typing import List


from chess.geometry.quadrant import Quadrant
from chess.motion.abstract.motion_controller import MotionController
from chess.motion.abstract.walk import Walk
from chess.motion.abstract.search_pattern import SearchPattern


class PawnMotionController(MotionController):
    def _apply_move_logic(self, piece: 'ChessPiece', board: 'ChessBoard', destination: 'Coordinate'):
        origin = piece.current_positio()
        if not self.walk.is_walkable(origin, destination):
            raise ValueError(f"{piece.label} cannot reach destination {destination} from origin {origin}.")

        board.capture_square(piece, destination)

    def _generate_moves_from_pattern(self, piece: 'ChessPiece', board: 'ChessBoard') -> List['Coordinate']:
        return self.search_pattern.search(piece, board)


    def __init__(
            self,
            name: str,
            letter: str,
            walk: Walk,
            search_pattern: SearchPattern,
            capture_value: int,
            number_per_team: int,
            territories: List[Quadrant]
        ):
        from chess.motion.pawn.service.pawn_motion_service import PawnMotionService
        super().__init__(
            name=name,
            letter=letter,
            walk=walk,
            search_pattern=search_pattern,
            capture_value=capture_value,
            territories=territories,
            number_per_team=number_per_team
        )

