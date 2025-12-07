# src/chess/team/service/data/exception/base.py

"""
Module: chess.team.entity_service.data.exception.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import DataException

__all__ = [
# ======================# TEAM_DATA EXCEPTION SUPER CLASS #======================#
    "TeamDataException",
]

# ======================# TEAM_DATA EXCEPTION SUPER CLASS #======================#
class TeamDataException(DataException):
    """
    Catchall for TeamData exceptions. Use as a last resort if TeamInsertionFailed or
    TeamDeletionFailedExceptions are not a good fit. Subclasses give better debugging info.
    """
    ERROR_CODE = "TEAM_DATA_COLLECTION_OPERATION_ERROR"
    DEFAULT_MESSAGE = "A CRUD operation on the Team data set raised an exception."