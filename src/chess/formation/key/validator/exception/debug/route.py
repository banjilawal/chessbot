# src/chess/formation/validator/exception/debug/route.py

"""
Module: chess.formation.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_FORMATION_SUPER_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "FormationSuperKeyValidationRouteException",
]


# ======================# UNHANDLED_FORMATION_SUPER_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class FormationSuperKeyValidationRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that FormationSuperKeyValidator did not handle one of the paths necessary to assure a candidate is a
        safe to use FormationSuperKey. There are different configurations of FormationSuperKey that are correct. Each
        configuration must have a testing route for a thorough verification process. If a FormationSuperKey configuration
        does not have a validation route the last step in the logic will return a ValidationResult containing a
        FormationSuperKeyValidationRouteException.

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
    ERROR_CODE = "UNHANDLED_FORMATION_SUPER_KEY_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The FormationSuperKeyValidator did not handle one of the paths necessary to assure a candidate is a safe to use"
        "FormationSuperKey. Ensure all possible verification branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-verification-blocks."
    )