__all__ = [
    # ======================# NO_ANALYSIS_ROUTE_FOR_STATE_CONDITION EXCEPTION #======================#
    "NoAnalysisRouteException",
]

from chess.system import NoExecutionRouteException


# ======================# NO_ANALYSIS_ROUTE_FOR_STATE_CONDITION EXCEPTION #======================#
class NoAnalysisRouteException(NoExecutionRouteException):
    """
    # ROLE: Error Tracing, Debugging, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an analysis failed because there was no execution route for a certain state.

    # PARENT:
        *   NoExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_ANALYSIS_ROUTE_FOR_STATE_CONDITION_ERROR"
    DEFAULT_MESSAGE = "Analysis failed: No analysis route was defined for a certain state."