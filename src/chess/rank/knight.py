from chess.board import Board
from chess.coord import Coord
from chess.piece import Piece
from chess.rank import Rank, RankSpec
from chess.vector import Vector


class Knight(Rank):
    
    def __init__(self, spec: RankSpec = RankSpec.KNIGHT):
        super().__init__(
            id=spec.id,
            name=spec.name,
            letter=spec.letter,
            ransom=spec.ransom,
            quadrants=spec.quadrants,
            quota=spec.quota
        )
    
    @classmethod
    def compute_span(cls, origin: Coord) -> [Coord]:
        return [
            origin.add_vector(Vector(1, 2)),
            origin.add_vector(Vector(-1, 2)),
            origin.add_vector(Vector(1, -2)),
            origin.add_vector(Vector(-1, -2)),
            origin.add_vector(Vector(2, 1)),
            origin.add_vector(Vector(2, -1)),
            origin.add_vector(Vector(-2, 1)),
            origin.add_vector(Vector(-2, -1))
        ]
    
    def walk(self, piece: Piece, destination: Coord, board: Board):
        """"""
        # method = "Knight.walk"
        #
        # try:
        #   if not Path(piece.current_position, destination).line == Line.KNIGHT:
        #     raise KnightWalkException(f"{method}: {KnightWalkException.DEFAULT_MESSAGE}")
        #
        #   square = board.find_square_by_coord(destination)
        #   OccupationFlow.enter(
        #     board=board,
        #     request=OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
        #   )
        # except KnightWalkException as e:
        #   raise KnightException(f"{method}: {KnightException.DEFAULT_MESSAGE}") from e
