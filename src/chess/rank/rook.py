from chess.rank import Rank, RankSpec


class Rook(Rank):

    def __init__(self, spec: RankSpec=RankSpec.BISHOP):
        super().__init__(
            name=spec.name,
            letter=spec.letter,
            ransom=spec.ransom,
            quadrants=spec.quadrants,
            quota=spec.quota
        )


    def walk(self, piece: Piece, destination: Coord, board: Board):
        method = "Rook.walk"
        try:
            path = Path(piece.current_position, destination)
            if not path.line == Line.ROOK:
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

