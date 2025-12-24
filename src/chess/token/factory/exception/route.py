from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_PIECE_BUILD_ROUTE EXCEPTION #======================#
    "PieceBuildRouteException",
]


# ======================# UNHANDLED_PIECE_BUILD_ROUTE EXCEPTION #======================#
class PieceBuildRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that PieceFactory did not handle one of the product build paths. The factory does not 
        have a production line for all the concrete Piece products. last step in the logic will return a
        BuildResult containing a PieceBuildRouteException.

    # PARENT:
        *   ResultException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_PIECE_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The PieceFactory does not have a production line for all concrete Piece classes. Ensure all build branches a"
        "re covered to prevent the execution flow from hit the default failure result outside the if-blocks."
    )