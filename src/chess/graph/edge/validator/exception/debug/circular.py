from chess.graph import EdgeException
from chess.system import DebugException


class CircularEdgeException(EdgeException, DebugException):
    pass