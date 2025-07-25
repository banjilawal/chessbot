from chess.common.geometry import Coordinate, Delta
from chess.motion.quadrant import Quadrant




class Walk:
    _pattern

    @staticmethod
    def horizontal_walk(self, origin: Coordinate, delta: Delta, number_of_steps: int) -> list[Coordinate]:
        points = []
        theta = Delta(x=delta.x, y=0)
        for i in range(number_of_steps):
            points.append(origin.shift(theta * i))
        return points

    @staticmethod
    def vertical_walk(self, origin: Coordinate, delta: Delta, number_of_steps: int) -> list[Coordinate]:
        points = []
        theta = Delta(x=0, y=delta.y)
        for i in range(number_of_steps):
            points.append(origin.shift(theta * i))
        return points

    @staticmethod
    def diagonal_walk(self, origin: Coordinate, delta: Delta, number_of_steps: int) -> list[Coordinate]:
        points = []
        for i in range(number_of_steps):
            points.append(origin.shift(delta * i))
        return points

    @staticmethod
    def bishop_walk(self, origin: Coordinate, number_of_steps: int) -> list[Coordinate]:
        points = []
        i = 0
        for q in [Quadrant.NE, Quadrant.NW, Quadrant.SW, Quadrant.SE]:
            points.extend(self.diagonal_walk(origin, Delta(q.x_delta, q.y_delta), number_of_steps))
            i += 1
            if i >= number_of_steps:
                break
        return points

    @staticmethod
    def castle_walk(self, origin: Coordinate, number_of_steps) -> list[Coordinate]:
        points = []
        i = 0
        for q in [Quadrant.N, Quadrant.S]:
            points.extend(self.vertical_walk(origin, Delta(q.x_delta, q.y_delta), number_of_steps))
            i += 1
            if i >= number_of_steps:
                break
        for q in [Quadrant.E, Quadrant.W]:
            points.extend(self.horizontal_walk(origin, Delta(q.x_delta, q.y_delta), number_of_steps))
            i += 1
            if i >= number_of_steps:
                break
        return points

    @staticmethod
    def queen_walk(self, origin: Coordinate, number_of_steps) -> list[Coordinate]:
        points = []
        points.extend(self.bishop_walk(origin, number_of_steps))
        points.extend(self.castle_walk(origin, number_of_steps))
        return points

    @staticmethod
    def king_walk(self, origin: Coordinate) -> list[Coordinate]:
        return self.queen_walk(origin, 1)

    @staticmethod
    def pawn_walk(self, origin: Coordinate) -> list[Coordinate]:
        return [
            origin.shift(Delta(y=1, x=0)),
            origin.shift(Delta(y=2, x=1)),
            origin.shift(Delta(y=2, x=-1))
        ]

    @staticmethod
    def knight_walk (self, origin: Coordinate) -> list[Coordinate]:
        return [
            origin.shift(Delta(y=3, x=1)),
            origin.shift(Delta(y=3, x=-1)),
            origin.shift(Delta(y=-3, x=1)),
            origin.shift(Delta(y=-3, x=-1))
        ]
#
# def linear_walk(
#     origin: Coordinate,
#     x_delta: int,
#     y_delta: int,
#     board: Board,
#     max_steps: int = None
# ) -> List[Coordinate]:
#     positions = []
#     current = origin.shift(x_delta, y_delta)
#     steps = 0
#
#     while board.coordinate_is_valid(current):
#         occupant = board.get_chess_piece_by_coordinate(current)
#         if occupant:
#             positions.append(current)  # Could be a capture
#             break
#
#         positions.append(current)
#         current = current.shift(x_delta, y_delta)
#         steps += 1
#
#         if max_steps is not None and steps >= max_steps:
#             break
#
#     return positions
#
#
# def diagonal_walk(
#         origin: Coordinate,
#         x_delta: int,
#         y_delta: int,
#         board: Board,
#         max_steps: int = None
# ) -> list[Coordinate]:
#     positions = []
#     current = origin.shift(x_delta, y_delta)
#     steps = 0
#
#     while board.coordinate_is_valid(current):
#         occupant = board.get_chess_piece_by_coordinate(current)
#         if occupant is None:
#             positions.append(current)
#         else:
#             break
#         current = current.shift(x_delta, y_delta)
#         steps += 1
#
#         if max_steps is not None and steps >= max_steps:
#             break
#     return positions