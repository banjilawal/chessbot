# src/chess/house/__init__.py

"""
Module: chess.house.__init__
Author: Banji Lawal
Created: 2025-11-10
version: 1.0.0
"""

from chess.system import (
    ChessException, NullException, ValidationException, BuildFailedException, InconsistencyException
)

__all__ = [
    "HouseException",
    
# ====================== HOUSE VALIDATION EXCEPTIONS #======================#
    "NullHouseException",
    "InvalidHouseException",
    "TurnSceneActorSquareIsNullException",
    "NullHouseResidentException",
    
    # ====================== TURN_SCENE BUILD EXCEPTIONS #======================#
    "HouseBuildFailedException",
]


class HouseException(ChessException):
    ERROR_CODE = "HOUSE_ERROR"
    DEFAULT_MESSAGE = "A House raised an exception"


# ====================== HOUSE GENERAL VALIDATION EXCEPTIONS #======================#
class NullHouseException(HouseException, NullException):
    """"""
    ERROR_CODE = "NULL_HOUSE_ERROR"
    DEFAULT_MESSAGE = "A House cannot be null."


class InvalidHouseException(HouseException, ValidationException):
    """"""
    ERROR_CODE = "HOUSE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "House validation failed."


class TurnSceneActorSquareIsNullException(HouseException):
    """"""
    ERROR_CODE = "HOUSE_SQUARE_IS_NULL_ERROR"
    DEFAULT_MESSAGE = "A House object cannot have a validation square."


class NullHouseResidentException(HouseException):
    """"""
    ERROR_CODE = "HOUSE_RESIDENT_IS_NULL_ERROR"
    DEFAULT_MESSAGE = "A House instance cannot have a validation occupant."


# ====================== HOUSE BUILD EXCEPTIONS #======================#
class HouseBuildFailedException(HouseException, BuildFailedException):
    """"""
    ERROR_CODE = "HOUSE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "House build failed."