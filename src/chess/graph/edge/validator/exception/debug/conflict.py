from chess.graph import EdgeException
from chess.system import DebugException


class HeadCannotBeTailException(EdgeException, DebugException):
    pass