# src/chess/rank/validator/entity_service.py

"""
Module: chess.rank.validator.entity_service
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""
from typing import Any

from chess.system import ValidationResult, Validator
from chess.rank import Rank, RankSpecValidator, RankValidatorFactory

class RankValidatorService(Validator[Rank]):
    _rank_validator: RankValidatorFactory
    _rank_spec_validator: RankSpecValidator
    
    def __init__(
            self,
            rank_spec_validator: RankSpecValidator = RankSpecValidator(),
            rank_validator: RankValidatorFactory = RankValidatorFactory(),
    ):
        super().__init__()
        self._rank_validator = rank_validator
        self._rank_spec_validator = rank_spec_validator

    @property
    def rank_validator(self) -> RankValidatorFactory:
        return self._rank_validator
        
    @property
    def rank_spec_validator(self) -> RankSpecValidator:
        return self._rank_spec_validator
    
    @classmethod
    def validate(cls, candidate: Any, *args, **kwargs) -> ValidationResult[Rank]:
        factory = RankValidatorFactory()
        return factory.validate(candidate)
    