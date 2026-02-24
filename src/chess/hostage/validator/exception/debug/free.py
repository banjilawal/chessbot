# ======================# FREE_AND_ACTIVE_ENEMY_CANNOT_BE_PRISONER EXCEPTION #======================#
from chess.hostage import HostageException


class PrisonerCannotBeActiveCombatantException(HostageException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a occupant cannot be added to t

    # PARENT:
        *   HostageException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FREE_AND_ACTIVE_ENEMY_CANNOT_BE_PRISONER_ERROR"
    DEFAULT_MESSAGE = "Hostage validation failed: An enemy cannot be a prisoner if its status is free."