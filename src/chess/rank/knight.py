

class Knight(Rank):

    def __init__(
        self,
        name:str=RankProfile.KNIGHT.name,
        letter:str=RankProfile.KNIGHT.letter,
        value:int=RankProfile.KNIGHT.value,
        per_side:int=RankProfile.KNIGHT.per_side,
        quadrants:[Quadrant]=RankProfile.KNIGHT.quadrants
    ):
        super().__init__(name=name, letter=letter, value=value, quadrants=quadrants, per_side=per_side)


    def walk(self, piece: Piece, destination: Coord, board: Board):
        method = "Knight.walk"

        try:
            if not Path(piece.current_position, destination).line == Line.KNIGHT:
                raise KnightWalkException(f"{method}: {KnightWalkException.DEFAULT_MESSAGE}")

            square = board.find_square_by_coord(destination)
            OccupationFlow.enter(
                board=board,
                request=OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
            )
        except KnightWalkException as e:
            raise KnightException(f"{method}: {KnightException.DEFAULT_MESSAGE}") from e


