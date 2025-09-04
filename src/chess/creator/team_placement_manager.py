from typing import List, TYPE_CHECKING


from chess.exception.id import ChessException
from chess.config.placement import PlacementChart
from chess.token.model import Piece

if TYPE_CHECKING:
    from chess.arena.model import Arena

class PlacementException(ChessException):
    default_message = "Placemen failed"

class TeamPlacementManager:

    @staticmethod
    def place_teams(arena: 'Arena'):
        method = "TeamPlacementManager.place_teams"

        chess_pieces: List[Piece] = []
        chess_pieces.extend(arena.white_owner.team.pieces)
        chess_pieces.extend(arena.black_owner.team.pieces)

        for chess_piece in chess_pieces:
                # .black_owner.side.chess_pieces):
            # print("placing", captor.name)
            for placement in PlacementChart:
                # print("checking placement", placement.value[0])
                square_name = placement.find_placement_by_piece(chess_piece)
                # print("expecting square named", square_name)
                if square_name is not None:
                    square = arena.chess_board.find_square_by_name(square_name)
                    # print("found square", square)
                    square.occupant = chess_piece
                    chess_piece.positions.push_coord(square.coord)
                    # print(square)



