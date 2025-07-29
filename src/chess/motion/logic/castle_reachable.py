
from chess.geometry.coordinate import Coordinate
from chess.geometry.horizontal import Horizontal
from chess.geometry.vertical import Vertical
from chess.motion.logic.reachable import Reachable



class CastleReachable(Reachable):

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        return Vertical.is_vertical(origin, destination) or Horizontal.is_horizontal(origin, destination)


    # def _perform_search(self, piece: Piece, board: Board) -> List[Coordinate]:
    #     destinations = []
    #     origin = piece.current_position()
    #     for quadrant in [Quadrant.N, Quadrant.E, Quadrant.S, Quadrant.W]:
    #         x_delta = quadrant.x_delta
    #         y_delta = quadrant.y_delta
    #         next_coord = origin.shift(x_delta, y_delta)
    #
    #         while next_coord.column < ROW_SIZE and next_coord.row < ROW_SIZE:
    #
    #             occupant = board.get_piece_by_coordinate(next_coord)
    #             if occupant is not None:
    #                 if not piece.is_enemy(occupant):
    #                     break
    #                 else:
    #                     destinations.append(next_coord)
    #                     break
    #             else:
    #                 destinations.append(next_coord)
    #             next_coord = next_coord.shift(x_delta, y_delta)
    #
    #     return destinations
