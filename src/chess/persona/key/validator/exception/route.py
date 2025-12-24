from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_PERSONA_SUPER_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "PersonaSuperKeyValidationRouteException",
]


# ======================# UNHANDLED_PERSONA_SUPER_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class PersonaSuperKeyValidationRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that PersonaSuperKeyValidator did not handle one of the paths necessary to assure a candidate is a
        safe to use PersonaSuperKey. There are different configurations of PersonaSuperKey that are correct. Each
        configuration must have a testing route for a thorough verification process. If a PersonaSuperKey configuration
        does not have a validation route the last step in the logic will return a ValidationResult containing a
        PersonaSuperKeyValidationRouteException.

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
    ERROR_CODE = "UNHANDLED_PERSONA_SUPER_KEY_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The PersonaSuperKeyValidator did not handle one of the paths necessary to assure a candidate is a safe to use"
        "PersonaSuperKey. Ensure all possible verification branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-verification-blocks."
    )