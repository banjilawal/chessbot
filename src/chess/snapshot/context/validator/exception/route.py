__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "SnapshotContextValidationRouteException",
]

from chess.system import ResultException, UnhandledRouteException


# ======================# UNHANDLED_SNAPSHOT_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class SnapshotContextValidationRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that SnapshotContextValidator did not handle one of the paths necessary to assure a candidate is a
        safe to use SnapshotContext. There are different configurations of SnapshotContext that are correct. Each
        configuration must have a testing route for a thorough verification process. If a SnapshotContext configuration
        does not have a validation route the last step in the logic will return a ValidationResult containing a
        SnapshotContextValidationRouteException.

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
    ERROR_CODE = "UNHANDLED_SNAPSHOT_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The SnapshotContextValidator did not handle one of the paths necessary to assure a candidate is a safe to use"
        "SnapshotContext. Ensure all possible verification branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-verification-blocks."
    )