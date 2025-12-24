from chess.persona import PersonaException
from chess.system import LookupFailedException

__all__ = [
    # ======================# PERSONA_LOOKUP_FAILURE EXCEPTION #======================#
    "PersonaLookupFailedException",
]


# ======================# PERSONA_LOOKUP_FAILURE EXCEPTION #======================#
class PersonaLookupFailedException(PersonaException, LookupFailedException):
    """
    # ROLE: ExceptionWrapper, Encapsulation

    # RESPONSIBILITIES:
    1.  If a Persona lookup runs into an error a debug exception is created and encapsulated in a
        PersonaLookupFailedException creating an exception chain which is sent to the caller in a
        SearchResult.
    2.  The PersonaLookupFailedException chain is useful for tracing a failure to its source.

    # PARENT:
        *   InvalidPersonaException
        *   LookupServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_LOOKUP_FAILURE"
    DEFAULT_MESSAGE = "Persona lookup failed."

