# src/logic/rank/validator/service.py

"""
Module: logic.rank.validator.service
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""
from typing import Any

from logic.system import ValidationResult, ValidationProcess
from logic.rank import Rank, RankSpecValidator, RankValidationProcessFactory

class RankValidationProcessService(ValidationProcess[Rank]):
    _rank_validator: RankValidationProcessFactory
    _rank_spec_validator: RankSpecValidator
    
    def __init__(
            self,
            rank_spec_validator: RankSpecValidator = RankSpecValidator(),
            rank_validator: RankValidationProcessFactory = RankValidationProcessFactory(),
    ):
        super().__init__()
        self._rank_validator = rank_validator
        self._rank_spec_validator = rank_spec_validator

    @property
    def rank_validator(self) -> RankValidationProcessFactory:
        return self._rank_validator
        
    @property
    def rank_spec_validator(self) -> RankSpecValidator:
        return self._rank_spec_validator
    
    @classmethod
    def validate(cls, candidate: Any, *args, **kwargs) -> ValidationResult[Rank]:
        factory = RankValidationProcessFactory()
        return factory.validate(candidate)
    