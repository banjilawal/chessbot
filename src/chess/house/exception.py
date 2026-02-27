# src/chess/house/__init__.py

"""
Module: chess.house.__init__
Author: Banji Lawal
Created: 2025-11-10
version: 1.0.0
"""

from chess.system import (
    ChessException, NullException, ValidationException, BuildException, InconsistencyException
)

__all__ = [
    "HouseException",
    
#====================== HOUSE VALIDATION EXCEPTION #======================#
    "NullHouseException",
    "InvalidHouseException",
    "TurnSceneActorSquareIsNullException",
    "NullHouseResidentException",
    
    #====================== TURN_SCENE BUILD EXCEPTION #======================#
    "HouseBuildException",
]


class HouseException(ChessException):
    ERR_CODE = "HOUSE_EXCEPTION"
    MSG = "A House raised an exception"


#====================== HOUSE GENERAL VALIDATION EXCEPTION #======================#
class NullHouseException(HouseException, NullException):
    """"""
    ERR_CODE = "NULL_HOUSE_EXCEPTION"
    MSG = "A House cannot be null."


class InvalidHouseException(HouseException, ValidationException):
    """"""
    ERR_CODE = "HOUSE_VALIDATION_EXCEPTION"
    MSG = "House validation failed."


class TurnSceneActorSquareIsNullException(HouseException):
    """"""
    ERR_CODE = "HOUSE_SQUARE_IS_NULL_EXCEPTION"
    MSG = "A House object cannot have a validation square_name."


class NullHouseResidentException(HouseException):
    """"""
    ERR_CODE = "HOUSE_RESIDENT_IS_NULL_EXCEPTION"
    MSG = "A House instance cannot have a validation occupant."


#====================== HOUSE BUILD EXCEPTION #======================#
class HouseBuildException(HouseException, BuildException):
    """"""
    ERR_CODE = "HOUSE_BUILD_FAILED"
    MSG = "House build failed."