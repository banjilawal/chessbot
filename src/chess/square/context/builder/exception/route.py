from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_SQUARE_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "SquareContextBuildRouteException",
]


# ======================# UNHANDLED_SQUARE_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class SquareContextBuildRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that SquareContextBuilder did not handle one of the paths necessary to assure a candidate is a
        safe to use SquareContext. There are different configurations of SquareContext that are correct. Each
        configuration must have a build route to guarantee all SquareContext products are safe. If a
        SquareContext configuration does not have a build route the last step in the logic will return a
        BuildResult containing a SquareContextBuildRouteException.

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
    ERROR_CODE = "UNHANDLED_SQUARE_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The SquareContextBuilder did not handle one of the paths necessary to guarantee SquareContexts are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )