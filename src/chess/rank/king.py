from chess.board.board import Board
from chess.rank.profile import RankProfile





class King(PromotedQueen):

    def __init__(
        self,
        name:str=RankProfile.KING.name,
        letter:str=RankProfile.KING.letter,
        value:int=RankProfile.KING.value,
        per_side:int=RankProfile.KING.per_side,
        quadrants:[Quadrant]=RankProfile.KING.quadrants
    ):
        super().__init__(name=name, letter=letter, value=value, quadrants=quadrants, per_side=per_side)


    def walk(self, piece: Piece, destination: Coord, board: Board):
        method = "King.walk"

        try:
            if not Path(piece.current_position, destination).line == Line.KING:
                raise KingWalkException(f"{method}: {KingWalkException.DEFAULT_MESSAGE}")

            square = board.find_square_by_coord(destination)
            OccupationFlow.enter(
                board=board,
                request=OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
            )
        except KingWalkException as e:
            raise KingException(f"{method}: {KingException.DEFAULT_MESSAGE}") from e