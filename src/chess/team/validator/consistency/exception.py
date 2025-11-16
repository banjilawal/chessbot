# src/chess/bounds/validator/exception.py

"""
Module: chess.bounds.validator.exception
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""


from chess.team import TeamException
from chess.system import NullException


__all__ = [
    "TeamFieldInconsistencyException",
    
    # ======================# TEAM_CONSISTENCY_TUPLE EXCEPTIONS #======================#
    "NullTeamConsistencyTupleException",
    
    # ======================# TEAM_FIELD_CONSISTENCY EXCEPTIONS #======================#
    "TeamColorInconsistencyException",
    "TeamNameInconsistencyException",
    "TeamLetterInconsistencyException",
    "AdvancingStepInconsistencyException",
    "TeamRankRowInconsistencyException",
    "TeamPawnRowInconsistencyException"
]


class TeamFieldInconsistencyException(TeamException):
    ERROR_CODE = "TEAM_FIELD_INCONSISTENCY_ERROR"
    DEFAULT_MESSAGE = "A Team property violated TeamSchema constraints. Ab exception was raised."


# ======================# TEAM_FIELD_CONSISTENCY_TUPLE EXCEPTIONS #======================#
class NullTeamConsistencyTupleException(TeamException, NullException):
    ERROR_CODE = "NULL_TEAM_CONSISTENCY_TUPLE_ERROR"
    DEFAULT_MESSAGE = "Tuple for checking Team-Field consistency cannot be null."


# ======================# TEAM_FIELD_CONSISTENCY EXCEPTIONS #======================#
class TeamColorInconsistencyException(TeamException):
    ERROR_CODE = "TEAM_COLOR_CONSISTENCY_ERROR"
    DEFAULT_MESSAGE = "Team.color value does not match the color assigned to the Team object by TeamSchema."


class TeamNameInconsistencyException(TeamException):
    ERROR_CODE = "TEAM_NAME_CONSISTENCY_ERROR"
    DEFAULT_MESSAGE = "Team.visitor_name value does not match the visitor_name assigned to the Team object by TeamSchema."


class TeamLetterInconsistencyException(TeamException):
    ERROR_CODE = "TEAM_LETTER_CONSISTENCY_ERROR"
    DEFAULT_MESSAGE = "Team.designation value does not match the designation assigned to the Team object by TeamSchema."


class AdvancingStepInconsistencyException(TeamException):
    ERROR_CODE = "TEAM_ADVANCING_STEP_CONSISTENCY_ERROR"
    DEFAULT_MESSAGE = (
        "Team.advancing_step value does not match the advancing_step assigned to the Team object by TeamSchema."
    )


class TeamRankRowInconsistencyException(TeamException):
    ERROR_CODE = "TEAM_RANK_ROW_CONSISTENCY_ERROR"
    DEFAULT_MESSAGE = (
        "Team.rank_row value does not match the rank_row assigned to the Team object by TeamSchema."
    )


class TeamPawnRowInconsistencyException(TeamException):
    ERROR_CODE = "TEAM_PAWN_ROW_CONSISTENCY_ERROR"
    DEFAULT_MESSAGE = (
        "Team.pawn_row value does not match the pawn_row assigned to the Team object by TeamSchema."
    )
