# src/chess/team/entity_service/data/exception/data/base.py

"""
Module: chess.team.entity_service.data.exception.entity_service.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import DataException, NullException

__all__ = [
# ======================# TEAM_INSERTION_FAILED EXCEPTIONS #======================#
    "TeamInsertionFailedException",
    "AddingDuplicateTeamException",
    "CannotAddNullTeamException",
]

# ======================# TEAM_INSERTION_FAILED EXCEPTIONS #======================#
class TeamInsertionFailedException(TeamDataException):
    ERROR_CODE = "TEAM_INSERTION_ERROR"
    DEFAULT_MESSAGE = "Team insertion failed."

class AddingDuplicateTeamException(TeamInsertionFailedException):
    """Raised when trying to add a duplicate Team to a list of Teams."""
    ERROR_CODE = "DUPLICATE_TEAM_INSERTION_ERROR"
    DEFAULT_MESSAGE = "UniqueTeamDataService cannot add duplicate Teams to the list."

class CannotAddNullTeamException(TeamInsertionFailedException, NullException):
    ERROR_CODE = "INSERTING_NULL_TEAM_ERROR"
    DEFAULT_MESSAGE = "Cannot push a null Team into the dataset."