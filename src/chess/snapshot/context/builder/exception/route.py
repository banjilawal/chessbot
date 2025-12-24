from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_SNAPSHOT_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "SnapshotContextBuildRouteException",
]


# ======================# UNHANDLED_SNAPSHOT_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class SnapshotContextBuildRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that SnapshotContextBuilder did not handle one of the paths necessary to assure a candidate is a
        safe to use SnapshotContext. There are different configurations of SnapshotContext that are correct. Each
        configuration must have a build route to guarantee all SnapshotContext products are safe. If a
        SnapshotContext configuration does not have a build route the last step in the logic will return a
        BuildResult containing a SnapshotContextBuildRouteException.

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
    ERROR_CODE = "UNHANDLED_SNAPSHOT_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The SnapshotContextBuilder did not handle one of the paths necessary to guarantee SnapshotContexts are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )