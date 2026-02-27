# src/chess/schema/validator/exception/route.py

"""
Module: chess.schema.validator.exception.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.system import ResultException, NoExecutionRouteException


__all__ = [
    # ======================# NO_SCHEMA_VALIDATION_ROUTE EXCEPTION #======================#
    "SchemaValidationRouteException",
]


# ======================# NO_SCHEMA_VALIDATION_ROUTE EXCEPTION #======================#
class SchemaValidationRouteException(ResultException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging
    
    # RESPONSIBILITIES:
    1.  Indicate that SchemaValidator did not handle one of the paths necessary to assure a candidate is a
        safe to use Schema. There are different configurations of Schema that are correct. Each
        configuration must have a testing route for a thorough verification process. If a Schema configuration
        does not have a validation route the last step in the logic will return a ValidationResult containing a
        SchemaValidationRouteException.
    
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
    ERR_CODE = "NO_SCHEMA_VALIDATION_ROUTE_EXCEPTION"
    MSG = (
        "The SchemaValidator did not handle one of the paths necessary to assure a candidate is a safe to use"
        "Schema. Ensure all possible verification branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-verification-blocks."
    )