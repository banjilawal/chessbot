# src/model/state/binder/exception/black.py

"""
Module: model.state.binder.exception.black
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# BLACK_TEAM_HAS_WRONG_SCHEMA EXCEPTION #======================#
    "BlackTeamHasWrongSchemaException",
]



# ======================# BLACK_TEAM_HAS_WRONG_SCHEMA EXCEPTION #======================#
class BlackTeamHasWrongSchemaException(TeamBinderException):
    """
    Role:Super Exception

    Responsibilities:
    1.  Indicates that the black team in the binder does not have a black schema.

    Super Class:
        *   TeamBinderException

    Provides:

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "BLACK_TEAM_HAS_WRONG_SCHEMA_EXCEPTION"
    MSG = "Black Team does not have a black schema."