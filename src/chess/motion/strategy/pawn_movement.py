from chess.board.chess_board import ChessBoard
from chess.common.geometry import Coordinate
from chess.motion.diagonal import DiagonalMove
from chess.motion.move import Move
from chess.motion.strategy.movement_strategy import MovementStrategy
from chess.motion.vertical import VerticalMove


class PawnMovement(MovementStrategy):