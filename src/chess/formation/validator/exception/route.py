from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_FORMATION_VALIDATION_ROUTE EXCEPTION #======================#
    "SchemValidationUnhandledRouteException",
]


# ======================# UNHANDLED_FORMATION_VALIDATION_ROUTE EXCEPTION #======================#
class SchemValidationUnhandledRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that FormationValidator did not handle one of the paths necessary to assure a candidate is a 
        Formation safe to use. A Formation has different configurations that are correct. Each configuration has a testing 
        route. If a configuration does not have a validation route a SchemValidationUnhandledRouteException 
        will be returned in a ValidationResult.

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
    ERROR_CODE = "UNHANDLED_FORMATION_VALIDATION_ROUTE"
    DEFAULT_MESSAGE = (
        "The FormationValidator did not handle one of the paths necessary to assure a candidate is a Formation safe to use. "
        "Ensure all possible verification branches are covered to ensure the execution flow does not hit the default "
        "failure result outside the if-verification-blocks."
    )