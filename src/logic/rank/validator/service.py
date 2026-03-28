# src/logic/rank/validation/transaction.py

"""
Module: logic.rank.validation.service
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""
from typing import Any

from logic.system import ValidationResult, ValidationTransaction
from logic.rank import Rank, RankSpecValidator, RankValidationTransactionFactory

class RankValidationTransactionService(ValidationTransaction[Rank]):
    _rank_validator: RankValidationTransactionFactory
    _rank_spec_validator: RankSpecValidator
    
    def __init__(
            self,
            rank_spec_validator: RankSpecValidator = RankSpecValidator(),
            rank_validator: RankValidationTransactionFactory = RankValidationTransactionFactory(),
    ):
        super().__init__()
        self._rank_validator = rank_validator
        self._rank_spec_validator = rank_spec_validator

    @property
    def rank_validator(self) -> RankValidationTransactionFactory:
        return self._rank_validator
        
    @property
    def rank_spec_validator(self) -> RankSpecValidator:
        return self._rank_spec_validator
    
    @classmethod
    def execute(cls, candidate: Any, *args, **kwargs) -> ValidationResult[Rank]:
        factory = RankValidationTransactionFactory()
        return factory.execute(candidate)
    