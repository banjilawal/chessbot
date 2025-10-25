from chess.rank import  Rank, RankSpec

class Pawn(Rank):

  def __init__(self, spec: RankSpec=RankSpec.PAWN):
    super().__init__(
      name=spec.name,
      letter=spec.letter,
      ransom=spec.ransom,
      quadrants=spec.quadrants,
      quota=spec.quota
    )


  def walk(self, piece: Piece, destination: Coord, board: Board):
    method = "Pawn.walk"

    try:
      if not (
        self._is_opening(piece, destination) or
        self._is_advance(piece, destination) or
        self._is_attack(piece, destination)
      ):
        raise PawnWalkException(f"{method}: {PawnWalkException.DEFAULT_MESSAGE}")

      square = board.find_square_by_coord(destination)
      OccupationFlow.enter(
        board=board,
        request=OccupationRequest(req_id=id_emitter.occupy_id, piece=piece, square=square)
      )
    except PawnWalkException as e:
      raise PawnRankException(f"{method}: {PawnRankException.DEFAULT_MESSAGE}") from e


  @staticmethod
  def _is_opening(piece: Piece, destination: Coord):
    return piece.positions.size() == 1 and Path(piece.current_position, destination).line == Line.PAWN_OPENING


  @staticmethod
  def _is_advance(self, piece: Piece, destination: Coord):
    return piece.positions.size() >= 1 and Path(piece.current_position, destination).line == Line.PAWN_ADVANCE

  @staticmethod
  def _is_attack(self, piece: Piece, destination: Coord):
    return piece.positions.size() >= 1 and Path(piece.current_position, destination).line == Line.PAWN_ATTACK

