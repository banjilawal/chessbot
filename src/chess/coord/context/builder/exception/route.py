from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_COORD_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "CoordContextBuildRouteException",
]


# ======================# UNHANDLED_COORD_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class CoordContextBuildRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that CoordContextBuilder did not handle one of the paths necessary to assure a candidate is a
        safe to use CoordContext. There are different configurations of CoordContext that are correct. Each
        configuration must have a build route to guarantee all CoordContext products are safe. If a
        CoordContext configuration does not have a build route the last step in the logic will return a
        BuildResult containing a CoordContextBuildRouteException.

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
    ERROR_CODE = "UNHANDLED_COORD_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The CoordContextBuilder did not handle one of the paths necessary to guarantee CoordContexts are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )