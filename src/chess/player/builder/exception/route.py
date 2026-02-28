from chess.system import ResultException, ExecutionRouteException

__all__ = [
    # ======================# NO_PLAYER_BUILD_ROUTE EXCEPTION #======================#
    "PlayerBuildRouteException",
]


# ======================# NO_PLAYER_BUILD_ROUTE EXCEPTION #======================#
class PlayerBuildRouteException(ResultException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that PlayerFactory did not handle one of the product build paths. The factory does not 
        have a production line for all the concrete Player products. last step in the logic will return a
        BuildResult containing a PlayerBuildRouteException.

    # PARENT:
        *   ResultException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_PLAYER_BUILD_ROUTE_EXCEPTION"
    MSG = (
        "The PlayerFactory does not have a production line for all concrete Player classes. Ensure all build branches a"
        "re covered to prevent the execution flow from hit the default failure result outside the if-blocks."
    )