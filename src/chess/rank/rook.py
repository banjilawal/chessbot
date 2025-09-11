from chess.rank import Rank, RankProfile


class Rook(Rank):

    def __init__(
        self,
        name:str=RankProfile.CASTLE.name,
        letter:str=RankProfile.CASTLE.letter,
        value:int=RankProfile.CASTLE.value,
        per_side:int=RankProfile.CASTLE.per_side,
        quadrants:[Quadrant]=RankProfile.CASTLE.quadrants
    ):
        super().__init__(name=name, letter=letter, value=value, quadrants=quadrants, per_side=per_side)


    def walk(self, piece: Piece, destination: Coord, board: Board):
        method = "Rook.walk"
        try:
            path = Path(piece.current_position, destination)
            if not path.line == Line.CASTLE:
                raise CastleWalkException(f"{method}: {CastleWalkException.DEFAULT_MESSAGE}")

            square = board.find_square_by_coord(destination)
            OccupationFlow.enter(
                board=board,
                request=OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
            )
        except CastleWalkException as e:
            raise CastleException(f"{method}: {CastleException.DEFAULT_MESSAGE}") from e


def main():
    print(Rook())


if __name__ == "__main__":
    main()

