from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_AGENT_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "AgentContextBuildRouteException",
]


# ======================# UNHANDLED_AGENT_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class AgentContextBuildRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that AgentContextBuilder did not handle one of the paths necessary to assure a candidate is a
        safe to use AgentContext. There are different configurations of AgentContext that are correct. Each
        configuration must have a build route to guarantee all AgentContext products are safe. If a
        AgentContext configuration does not have a build route the last step in the logic will return a
        BuildResult containing a AgentContextBuildRouteException.

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
    ERROR_CODE = "UNHANDLED_AGENT_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The AgentContextBuilder did not handle one of the paths necessary to guarantee AgentContexts are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )