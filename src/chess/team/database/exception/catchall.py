# src/chess/team/database/exception/catchall.py

"""
Module: chess.team.database.exception.catchall
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
    ERROR_CODE = "TEAM_DATABASE_ERROR"
    DEFAULT_MESSAGE = "TeamDatabase raised an exception."