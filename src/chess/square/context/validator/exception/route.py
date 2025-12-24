__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "SquareContextValidationRouteException",
]

from chess.system import ResultException, UnhandledRouteException


# ======================# UNHANDLED_SQUARE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class SquareContextValidationRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that SquareContextValidator did not handle one of the paths necessary to assure a candidate is a
        safe to use SquareContext. There are different configurations of SquareContext that are correct. Each
        configuration must have a testing route for a thorough verification process. If a SquareContext configuration
        does not have a validation route the last step in the logic will return a ValidationResult containing a
        SquareContextValidationRouteException.

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
    ERROR_CODE = "UNHANDLED_SQUARE_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The SquareContextValidator did not handle one of the paths necessary to assure a candidate is a safe to use"
        "SquareContext. Ensure all possible verification branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-verification-blocks."
    )