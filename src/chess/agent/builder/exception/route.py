from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_AGENT_BUILD_ROUTE EXCEPTION #======================#
    "AgentBuildRouteException",
]


# ======================# UNHANDLED_AGENT_BUILD_ROUTE EXCEPTION #======================#
class AgentBuildRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that AgentFactory did not handle one of the product build paths. The factory does not 
        have a production line for all the concrete Agent products. last step in the logic will return a
        BuildResult containing a AgentBuildRouteException.

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
    ERROR_CODE = "UNHANDLED_AGENT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The AgentFactory does not have a production line for all concrete Agent classes. Ensure all build branches a"
        "re covered to prevent the execution flow from hit the default failure result outside the if-blocks."
    )