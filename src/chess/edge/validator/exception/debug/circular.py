from chess.edge import EdgeException
from chess.system import DebugException

__all__ = [
    # ======================# CIRCULAR_EDGE EXCEPTION #======================#
    "CircularEdgeException",
]

class CircularEdgeException(EdgeException, DebugException):
    pass