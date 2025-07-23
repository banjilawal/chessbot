from typing import List

from chess.board.chess_board import ChessBoard
from chess.common.geometry import Coordinate


def linear_walk(
    origin: Coordinate,
    x_delta: int,
    y_delta: int,
    board: ChessBoard,
    max_steps: int = None
) -> List[Coordinate]:
    positions = []
    current = origin.shift(x_delta, y_delta)
    steps = 0

    while board.coordinate_is_valid(current):
        occupant = board.get_chess_piece_by_coordinate(current)
        if occupant:
            positions.append(current)  # Could be a capture
            break

        positions.append(current)
        current = current.shift(x_delta, y_delta)
        steps += 1

        if max_steps is not None and steps >= max_steps:
            break

    return positions


def diagonal_walk(
        origin: Coordinate,
        x_delta: int,
        y_delta: int,
        board: ChessBoard
) -> list[Coordinate]:
    destinations = []
    current = origin.shift(x_delta, y_delta)

    while board.coordinate_is_valid(current):
        occupant = board.get_chess_piece_by_coordinate(current)
        if occupant is None:
            destinations.append(current)
        else:
            break
        current = current.shift(x_delta, y_delta)
    return destinations