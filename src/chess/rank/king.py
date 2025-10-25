from chess.board.board import Board
from chess.rank import  Rank, RankSpec





class King(Rank):

  def __init__(self, spec: RankSpec=RankSpec.KING):
    super().__init__(
      name=spec.name,
      letter=spec.letter,
      ransom=spec.ransom,
      quadrants=spec.quadrants,
      quota=spec.quota
    )


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