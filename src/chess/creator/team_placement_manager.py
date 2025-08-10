from chess.arena.arena import Arena
from chess.config.placement_chart import PlacementChart


class TeamPlacementManager:

    @staticmethod
    def place_teams(arena: Arena):
        for chess_piece in arena.black_owner.team.chess_pieces():
            for placement in PlacementChart:
                square_name = placement.map_chess_piece_to_square_name(chess_piece)
                if square_name is not None:
                    square = arena.chess_board.find_square_by_name(square_name)
                    square.occupy(chess_piece)

