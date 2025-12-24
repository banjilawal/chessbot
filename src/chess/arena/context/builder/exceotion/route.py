from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_ARENA_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "ArenaContextBuildRouteException",
]


# ======================# UNHANDLED_ARENA_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class ArenaContextBuildRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that ArenaContextBuilder did not handle one of the paths necessary to assure a candidate is a
        safe to use ArenaContext. There are different configurations of ArenaContext that are correct. Each
        configuration must have a build route to guarantee all ArenaContext products are safe. If a
        ArenaContext configuration does not have a build route the last step in the logic will return a
        BuildResult containing a ArenaContextBuildRouteException.

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
    ERROR_CODE = "UNHANDLED_ARENA_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The ArenaContextBuilder did not handle one of the paths necessary to guarantee ArenaContexts are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )