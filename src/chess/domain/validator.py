# src/chess/graph/domain/validator.py

"""
Module: chess.graph.domain.validator
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from typing import Any, cast

from chess.graph import Domain, NullDomainException
from chess.domain.exception import DomainMissingTreeException
from chess.piece import PieceValidator

from chess.system import ChessException, IdValidator, LoggingLevelRouter, Validator, ValidationResult


class DomainValidator(Validator[Domain]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Domain]:
        """"""
        method = "DomainValidator.validate"
        try:
            if candidate is None:
                return ValidationResult.failure(NullDomainException(f"{method}: {NullDomainException.DEFAULT_MESSAGE}"))
            
            if not isinstance(candidate, Domain):
                return ValidationResult.failure(
                    TypeError(f"{method}: Was expecting type {Domain}, got {type(candidate)} instead")
                )
            domain = cast(Domain, candidate)
            
            id_validation = IdValidator.validate(domain.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            owner_validation = PieceValidator.validate(domain.owner)
            if owner_validation.is_failure():
                return ValidationResult.failure(owner_validation.exception)
            
            if domain.tree is None:
                return ValidationResult.failure(
                    DomainMissingTreeException(f"{method}: {DomainMissingTreeException.DEFAULT_MESSAGE}")
                )
            
            if domain.owner.current_position is None:
                return ValidationResult.failure(
                    ChessException(f"{method}: Cannot get the domain of a piece not on the board")
                )
            
            if domain.owner.current_position != domain.owner_address:
                return ValidationResult.failure(
                    ChessException(f"{method}: Domain current position and address are inconsistent")
                )
            
            return ValidationResult.success(domain)
        except Exception as e:
            return ValidationResult.failure(e)
