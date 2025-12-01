# src/chess/rank/validator/service.py

"""
Module: chess.rank.validator.service
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""
from typing import Any

from chess.system import ValidationResult, Validator
from chess.rank import Rank, RankSpecValidator, RankValidatorFactory

class RankValidatorService(Validator[Rank]):
    _spec_validator: RankSpecValidator
    
    def __init__(self, spec_validator: RankSpecValidator = RankSpecValidator()):
        self._spec_validator = spec_validator
        
    @property
    def spec_validator(self) -> RankSpecValidator:
        return self._spec_validator
    
    @classmethod
    def validate(cls, candidate: Any, *args, **kwargs) -> ValidationResult[Rank]:
        factory = RankValidatorFactory()
        return factory.validate(candidate)
    