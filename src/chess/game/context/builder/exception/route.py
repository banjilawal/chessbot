from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_GAME_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "GameContextBuildRouteException",
]


# ======================# UNHANDLED_GAME_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class GameContextBuildRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that GameContextBuilder did not handle one of the paths necessary to assure a candidate is a
        safe to use GameContext. There are different configurations of GameContext that are correct. Each
        configuration must have a build route to guarantee all GameContext products are safe. If a
        GameContext configuration does not have a build route the last step in the logic will return a
        BuildResult containing a GameContextBuildRouteException.

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
    ERROR_CODE = "UNHANDLED_GAME_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The GameContextBuilder did not handle one of the paths necessary to guarantee GameContexts are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )