__all__ = [
    # ======================# POPPING_EMPTY_ROSTER EXCEPTION #======================#
    "PoppingEmptyRosterException",
]


# ======================# POPPING_EMPTY_ROSTER EXCEPTION #======================#
class PoppingEmptyRosterException(TeamRosterException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a roster member failed because the roster was empty.

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_ROSTER_ERROR"
    DEFAULT_MESSAGE = "Roster member deletion failed: The roster is empty. Nothing to delete."