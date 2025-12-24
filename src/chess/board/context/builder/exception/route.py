from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_BOARD_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "BoardContextBuildRouteException",
]


# ======================# UNHANDLED_BOARD_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class BoardContextBuildRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that BoardContextBuilder did not handle one of the paths necessary to assure a candidate is a
        safe to use BoardContext. There are different configurations of BoardContext that are correct. Each
        configuration must have a build route to guarantee all BoardContext products are safe. If a
        BoardContext configuration does not have a build route the last step in the logic will return a
        BuildResult containing a BoardContextBuildRouteException.

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
    ERROR_CODE = "UNHANDLED_BOARD_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The BoardContextBuilder did not handle one of the paths necessary to guarantee BoardContexts are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )