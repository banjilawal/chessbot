# src/chess/team/validator/bounds/exception.py

"""
Module: chess.team.validator.bounds.exception
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""


from chess.system import NullException
from chess.team import TeamException, InvalidTeamException


__all__ = [
    "TeamBoundsException",
    
    # ======================# TEAM_ADVANCING_STEP VALIDATION EXCEPTIONS #======================#
    "AdvancingStepException",
    "NullAdvancingStepNullException",
    "AdvancingStepBoundsException",
    
    # ======================# TEAM_LETTER_FIELD VALIDATION EXCEPTIONS #======================#
    "TeamLetterException",
    "NullTeamLetterException",
    "TeamLetterBoundsException",
    
    # ======================# TEAM_NAME_FIELD VALIDATION EXCEPTIONS #======================#
    "TeamNameException",
    "TeamNameBoundsException",
    
    # ======================# TEAM_RANK_ROW_FIELD VALIDATION EXCEPTIONS #======================#
    "TeamRankRowException",
    "RankRowNullException",
    "RankRowBelowBoundsException",
    "RankRowAboveBoundsException",
    
    # ======================# TEAM_PAWN_ROW VALIDATION EXCEPTIONS #======================#
    "TeamPawnRowException",
    "PawnRowNullException",
    "PawnRowBelowBoundsException",
    "PawnRowAboveBoundsException",
    
    # ======================# TEAM_COLOR_FIELD VALIDATION EXCEPTIONS #======================#
    "TeamColorException",
    "TeamColorBoundsException"
]


class TeamBoundsException(InvalidTeamException):
    ERROR_CODE = "TEAM_FIELD_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The field of a Team object is outside the bounds declared in TeamSchema."


# ======================# TEAM_ADVANCING_STEP VALIDATION EXCEPTIONS #======================#
class AdvancingStepException(TeamBoundsException):
    ERROR_CODE = "ADVANCING_STEP_FIELD_ERROR"
    DEFAULT_MESSAGE = "The advancing_step property of a Team object violates TeamSchema constraints"


class NullAdvancingStepNullException(AdvancingStepException, NullException):
    ERROR_CODE = "NULL_ADVANCING_STEP_NULL_ERROR"
    DEFAULT_MESSAGE = "The advancing_step property of a Team cannot be null."


class AdvancingStepBoundsException(TeamBoundsException):
    ERROR_CODE = "TEAM_ADVANCING_STEP_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The Team.advancing_step field is outside the bounds declared in TeamSchema."


# ======================# TEAM_LETTER_FIELD VALIDATION EXCEPTIONS #======================#
class TeamLetterException(TeamException):
    ERROR_CODE = "TEAM_LETTER_FIELD_ERROR"
    DEFAULT_MESSAGE = "The Team.schema.letter raised an exception."


class NullTeamLetterException(TeamLetterException, NullException):
    ERROR_CODE = "NULL_TEAM_RANSOM_ERROR"
    DEFAULT_MESSAGE = "A Team.letter property cannot be null."


class TeamLetterBoundsException(TeamBoundsException):
    ERROR_CODE = "TEAM_LETTER_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The Team.letter property violates TeamSchema constraints."


# ======================# TEAM_NAME_FIELD VALIDATION EXCEPTIONS #======================#
class TeamNameException(TeamException):
    ERROR_CODE = "TEAM_NAME_FIELD_ERROR"
    DEFAULT_MESSAGE = "Name field of a Team object raised an exception."


class TeamNameBoundsException(TeamBoundsException):
    ERROR_CODE = "TEAM_NAME_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The Team.name property violates TeamSchema constraints."


# ======================# TEAM_RANK_ROW_FIELD VALIDATION EXCEPTIONS #======================#
class TeamRankRowException(TeamBoundsException):
    ERROR_CODE = "TEAM_QUOTA_FIELD_ERROR"
    DEFAULT_MESSAGE = "The quota of a Team object is outside the bounds declared in TeamSpec."


class RankRowNullException(TeamRankRowException, NullException):
    ERROR_CODE = "NULL_TEAM_QUOTA_ERROR"
    DEFAULT_MESSAGE = "A Team object cannot have a null quota."


class RankRowBelowBoundsException(TeamRankRowException):
    ERROR_CODE = "TEAM_QUOTA_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "A Team instance cannot have a quota below one."


class RankRowAboveBoundsException(TeamRankRowException):
    ERROR_CODE = "TEAM_QUOTA_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The Pawn has the highest quota. The value is above quota bounds."


# ======================# TEAM_PAWN_ROW VALIDATION EXCEPTIONS #======================#
class TeamPawnRowException(TeamBoundsException):
    ERROR_CODE = "TEAM_PAWN_ROW_FIELD_ERROR"
    DEFAULT_MESSAGE = "The quota of a Team object is outside the bounds declared in TeamSpec."


class PawnRowNullException(TeamPawnRowException, NullException):
    ERROR_CODE = "TEAM_PAWN_ROW_NULL_ERROR"
    DEFAULT_MESSAGE = "The pawn_row of a TeamSchema cannot be null."


class PawnRowBelowBoundsException(TeamPawnRowException):
    ERROR_CODE = "TEAM_PAWN_ROW_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "A Team instance cannot have a quota below one."


class PawnRowAboveBoundsException(TeamPawnRowException):
    ERROR_CODE = "TEAM_PAWN_ROW_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The Pawn has the highest quota. The value is above quota bounds."


# ======================# TEAM_LETTER_FIELD VALIDATION EXCEPTIONS #======================#
class TeamLetterException(InvalidTeamException):
    ERROR_CODE = "TEAM_LETTER_FIELD_ERROR"
    DEFAULT_MESSAGE = "The letter field of a Team object raised an exception."


class NullTeamLetterException(TeamLetterException, NullException):
    ERROR_CODE = "NULL_TEAM_LETTER_ERROR"
    DEFAULT_MESSAGE = "A Team object cannot have a null letter field."


# ======================# TEAM_COLOR_FIELD VALIDATION EXCEPTIONS #======================#
class TeamColorException(InvalidTeamException):
    ERROR_CODE = "TEAM_COLOR_FIELD_ERROR"
    DEFAULT_MESSAGE = "The color field of a Team object raised an exception."


class TeamColorBoundsException(TeamBoundsException):
    ERROR_CODE = "TEAM_LETTER_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The letter is not included in the Team letter specifications."
