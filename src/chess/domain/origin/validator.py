# src/chess/domain/origin/validator.py

"""
Module: chess.domain.origin.validator
Author: Banji Lawal
Created: 2025-11-11
version: 1.0.0
"""


from typing import Any, cast

from chess.domain import DomainOrigin, NullDomainOriginException
from chess.system import LoggingLevelRouter, Validator, ValidationResult



class DomainOriginValidator(Validator[DomainOrigin]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[DomainOrigin]:
        """"""
        method = "DomainOriginValidator.validate"
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullDomainOriginException(f"{method}: {NullDomainOriginException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, DomainOrigin):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected DomainOrigin, got {type(candidate).__name__} instead.")
                )
            
            domain_origin = cast(DomainOrigin, candidate)
            
            ValidationResult.success(payload=domain_origin)
        except Exception as e:
            return ValidationResult.failure(e)