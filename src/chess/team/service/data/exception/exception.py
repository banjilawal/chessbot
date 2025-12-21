# src/chess/team/service/data/exception/exception.py

"""
Module: chess.team.service.data.exception.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import DataSetException

__all__ = [
#======================# TEAM_DATA_SET EXCEPTION #======================#
    "TeamDataSetException",
]

#======================# TEAM_DATA_SET EXCEPTION #======================#
class TeamDataSetException(DataSetException):
    """
    Catchall for TeamData_set exception. Use as a last resort if TeamInsertionFailed or
    TeamDeletionFailedException are not a good fit. Subclasses give better debugging info.
    """
    ERROR_CODE = "TEAM_DATA_COLLECTION_OPERATION_ERROR"
    DEFAULT_MESSAGE = "A CRUD operation on the Team data set raised an exception."