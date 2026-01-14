__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "TokenContextValidationRouteException",
]

from chess.token import TokenException
from chess.system import UnhandledRouteException



# ======================# UNHANDLED_TOKEN_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class TokenContextValidationRouteException(TokenContextException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the TokenContext validation failed because there was no build route for the TokenContext key.

    # PARENT:
        *   TokenException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_TOKEN_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "TokenContext validation failed: No validation route was provided for the Token attribute."