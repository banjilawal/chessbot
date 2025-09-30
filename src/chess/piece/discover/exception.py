from chess.exception import ChessException, NullException, BuilderException

__all__ = [
    'DiscoveryException',
    'NullDiscoveryException',
    'DiscoveryBuilderException',
    'CircularDiscoveryException'
]

"""
Super class for Piece exceptions
"""
class DiscoveryException(ChessException):
    """
    Super class for exceptions raised by Discovery
    """
    ERROR_CODE = "DISCOVERY_ERROR"
    DEFAULT_MESSAGE = "Discovery instance raised an exception"


class NullDiscoveryException(DiscoveryException, NullException):
    """
    NullDiscoveryException is raised when a discover cannot be null.
    """
    ERROR_CODE = "NULL_DISCOVERY_ERROR"
    DEFAULT_MESSAGE = f"Discovery cannot be null"


class DiscoveryBuilderException(DiscoveryException, BuilderException):
    """
    Wrapper for exceptions raised when DiscoveryBuilder runs.
    """
    ERROR_CODE = "DISCOVERY_BUILDER_ERROR"
    DEFAULT_MESSAGE = "DiscoveryBuilder raised an exception"


class CircularDiscoveryException(DiscoveryException):
    """Raised if an observer scans itself."""
    ERROR_CODE = "OBSERVER_CIRCULAR_SCAN_ERROR"
    DEFAULT_MESSAGE = "An observer cannot discover itself"



"





