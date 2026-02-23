from chess.system import ResultException, NoExecutionRouteException

__all__ = [
    # ======================# NO_TOKEN_BUILD_ROUTE EXCEPTION #======================#
    "TokenBuildRouteException",
]


# ======================# NO_TOKEN_BUILD_ROUTE EXCEPTION #======================#
class TokenBuildRouteException(ResultException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that TokenFactory did not handle one of the product build paths. The factory does not 
        have a production line for all the concrete Token products. last step in the logic will return a
        BuildResult containing a TokenBuildRouteException.

    # PARENT:
        *   ResultException
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_TOKEN_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The TokenFactory does not have a production line for all concrete Token classes. Ensure all build branches a"
        "re covered to prevent the execution flow from hit the default failure result outside the if-blocks."
    )