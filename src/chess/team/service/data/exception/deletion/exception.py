# src/chess/team/service/data/exception/data/base.py

"""
Module: chess.team.entity_service.data.exception.entity_service.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import NullException
from chess.team import TeamDataException

__all__ = [
# ======================# TEAM_DELETION_FAILED EXCEPTIONS #======================#
    "TeamDeletionFailedException",
    "CannotRemoveNullTEamException",
]

# ======================# TEAM_DELETION_FAILED EXCEPTIONS #======================#
class TeamDeletionFailedException(TeamDataException):
    ERROR_CODE = "TEAM_DELETION_ERROR"
    DEFAULT_MESSAGE = "Team deletion failed."


class CannotRemoveNullTEamException(TeamDeletionFailedException, NullException):
    ERROR_CODE = "DELETING_NULL_TEAM_ERROR"
    DEFAULT_MESSAGE = "Cannot pull a team which does not exist in the dataset."