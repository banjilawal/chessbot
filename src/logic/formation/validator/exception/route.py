from logic.system import ResultException, ExecutionRouteException

__all__ = [
    # ======================# NO_FORMATION_VALIDATION_ROUTE EXCEPTION #======================#
    "SchemValidationExecutionRouteException",
]


# ======================# NO_FORMATION_VALIDATION_ROUTE EXCEPTION #======================#
class SchemValidationExecutionRouteException(ResultException, ExecutionRouteException):
    """
    Role:Fallback Result, Debugging

    Responsibilities:
    1.  Indicate that FormationValidationTransaction did not handle one of the paths necessary to assure a candidate is a
        Formation safe to use. A Formation has different configurations that are correct. Each configuration has a testing 
        route. If a configuration does not have a validation route a SchemValidationExecutionRouteException
        will be returned in a ValidationResult.

    Super Class:
        *   ResultException
        *   ExecutionRouteException

    # PROVIDES
    None


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_FORMATION_VALIDATION_ROUTE"
    MSG = (
        "The FormationValidationTransaction did not handle one of the paths necessary to assure a candidate is a Formation safe to use. "
        "Ensure all possible verification branches are covered to ensure the execution flow does not hit the default "
        "failure result outside the if-verification-blocks."
    )