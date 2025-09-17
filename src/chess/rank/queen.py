

class Queen(Rank):

    def __init__(
        self,
        name:str=RankProfile.QUEEN.name,
        letter:str=RankProfile.QUEEN.letter,
        value:int=RankProfile.QUEEN.value,
        per_side:int=RankProfile.QUEEN.per_side,
        quadrants:[Quadrant]=RankProfile.QUEEN.quadrants
    ):
        super().__init__(name=name, letter=letter, value=value, quadrants=quadrants, per_side=per_side)


    def walk(self, piece: Piece, destination: Coord, board: Board):
        method = "Queen.walk"

        try:
            if not Path(piece.current_position, destination).line == Line.QUEEN:
                raise QueenWalkException(f"{method}: {QueenWalkException.DEFAULT_MESSAGE}")

            square = board.find_square_by_coord(destination)
            OccupationFlow.enter(
                board=board,
                request=OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
            )
        except QueenWalkException as e:
            raise QueenRankException(f"{method}: {QueenRankException.DEFAULT_MESSAGE}") from e






