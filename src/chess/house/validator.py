# src/chess/house/coord_stack_validator.py

"""
Module: chess.house.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-10
version: 1.0.0
"""


from typing import Any, cast

from chess.square import SquareValidator
from chess.system import LoggingLevelRouter, Validator, ValidationResult
from chess.house import House, NullHouseException, NullHouseResidentException


class HouseValidator(Validator[House]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[House]:
        """"""
        method = "HouseValidator.validate"
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullHouseException(f"{method}: {NullHouseException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, House):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected House object received {candidate.__class__.__name__} instead")
                )
            
            house = cast(House, candidate)
            square_validation = SquareValidator.validate(house.square)
            if square_validation.is_failure():
                return ValidationResult.failure(square_validation.exception)
            
            
            if house.square.occupant is None:
                return ValidationResult.failure(
                    NullHouseResidentException(f"{method}: {NullHouseResidentException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(house)
        except Exception as e:
            return ValidationResult.failure(e)

