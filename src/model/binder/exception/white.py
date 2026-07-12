# src/model/state/binder/exception/white.py

"""
Module: model.state.binder.exception.white
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# WHITE_TEAM_HAS_WRONG_SCHEMA EXCEPTION #======================#
    "WhiteTeamHasWrongSchemaException",
]

from model.state.team import TeamBinderException


# ======================# WHITE_TEAM_HAS_WRONG_SCHEMA EXCEPTION #======================#
class WhiteTeamHasWrongSchemaException(TeamBinderException):
    """
    Role:Super Exception

    Responsibilities:
    1.  Indicates that the white team in the binder does not have a white schema.

    Super Class:
        *   TeamBinderException

    Provides:

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "WHITE_TEAM_HAS_WRONG_SCHEMA_EXCEPTION"
    MSG = "White Team does not have a white schema."