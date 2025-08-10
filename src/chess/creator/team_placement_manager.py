from typing import List

from chess.arena.arena import Arena
from chess.config.placement_chart import PlacementChart
from chess.token.chess_piece import ChessPiece


class TeamPlacementManager:

    @staticmethod
    def place_teams(arena: Arena):
        chess_pieces: List[ChessPiece] = []
        chess_pieces.extend(arena.white_owner.team.chess_pieces)
        chess_pieces.extend(arena.black_owner.team.chess_pieces)

        for chess_piece in chess_pieces:
                # .black_owner.team.chess_pieces):
            # print("placing", chess_piece.name)
            for placement in PlacementChart:
                # print("checking placement", placement.value[0])
                square_name = placement.map_chess_piece_to_square_name(chess_piece)
                # print("expecting square named", square_name)
                if square_name is not None:
                    square = arena.chess_board.find_square_by_name(square_name)
                    # print("found square", square)
                    square.occupant = chess_piece
                    # print(square)



