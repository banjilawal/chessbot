from typing import List, TYPE_CHECKING


from chess.exception.id.negative_id_exception import ChessException
from chess.config.placement import PlacementChart
from chess.piece.model.piece import Piece

if TYPE_CHECKING:
  from chess.arena.arena import Arena

class PlacementException(ChessException):
  default_message = "Placemen failed"

class TeamPlacementManager:

  @staticmethod
  def place_teams(arena: 'Arena'):
    method = "TeamPlacementManager.place_teams"

    chess_pieces: List[Piece] = []
    chess_pieces.extend(arena.white_owner.team.roster)
    chess_pieces.extend(arena.black_owner.team.roster)

    for chess_piece in chess_pieces:
        # .black_owner.team.chess_pieces):
      # print("placing", captor.visitor_name)
      for placement in PlacementChart:
        # print("checking placement", placement.value[0])
        square_name = placement.find_placement_by_piece(chess_piece)
        # print("expecting square named", square_name)
        if square_name is not None:
          square = arena.chess_board.find_square_by_name(square_name)
          # print("found square", square)
          square.occupant = chess_piece
          chess_piece.positions.push_coord(square.position)
          # print(square)



