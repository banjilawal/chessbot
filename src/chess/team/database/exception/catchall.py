# src/chess/team/database/exception/super.py

"""
Module: chess.team.database.exception.super
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

___all__ = [
    # ======================# TEAM_DATABASEEXCEPTION #======================#
    "TeamDatabaseException",
]

from chess.team import TeamException
from chess.system import ServiceException


# ======================# TEAM_DATABASE EXCEPTION #======================#
class TeamDatabaseException(TeamException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Encapsulate TeamDatabase method outputs when there is a failure.
    
    # PARENT:
        *   ServiceException
        *   TeamException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_DATABASE_EXCEPTION"
    MSG = "TeamDatabase raised an exception."