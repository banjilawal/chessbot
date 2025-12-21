# src/chess/team/service/data/exception/data/exception.py

"""
Module: chess.team.service.data.exception.service.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import NullException
from chess.team import TeamDatasetException

__all__ = [
#======================# TEAM_DELETION_FAILED EXCEPTION #======================#
    "TeamDeletionFailedException",
    "CannotRemoveNullTEamException",
]

#======================# TEAM_DELETION_FAILED EXCEPTION #======================#
class TeamDeletionFailedException(TeamDatasetException):
    ERROR_CODE = "TEAM_DELETION_ERROR"
    DEFAULT_MESSAGE = "Team deletion failed."


class CannotRemoveNullTEamException(TeamDeletionFailedException, NullException):
    ERROR_CODE = "DELETING_NULL_TEAM_ERROR"
    DEFAULT_MESSAGE = "Cannot pull a team which does not exist in the dataset."