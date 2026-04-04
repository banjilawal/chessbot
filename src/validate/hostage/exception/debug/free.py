# ======================# FREE_AND_ACTIVE_ENEMY_CANNOT_BE_PRISONER EXCEPTION #======================#
from model.hostage import HostageException


class PrisonerCannotBeActiveCombatantException(HostageException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a occupant cannot be added to t

    Super Class:
        *   HostageException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "FREE_AND_ACTIVE_ENEMY_CANNOT_BE_PRISONER_EXCEPTION"
    MSG = "Hostage validation failed: An enemy cannot be a prisoner if its status is free."