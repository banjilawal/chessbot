# src/chess/graph/owner/factory.py

"""
Module: chess.graph.owner.validator
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""


from typing import Any, cast

from chess.king import KingPiece
from chess.piece import CombatantPiece, PieceValidator
from chess.square import SquareValidator
from chess.system import ChessException, IdValidator, LoggingLevelRouter, Validator, ValidationResult
from chess.domain import (
    Domain, InvalidDomainException, NullDomainException, InconsistenDomainAddressException,
    PieceNotOnRosterDomainOwnerException,
    CapturedDomainOwnerException, CheckmatedKingDomainOwnerException, DomainMissingTreeException,
)




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
            
            owner_square_validation = SquareValidator.verify_piece_relates_to_square(
                domain.origin.square,
                domain.origin.owner
            )
            if owner_square_validation.is_failure():
                return ValidationResult.failure(owner_square_validation.exception)
            
            if domain.squares is None:
                return ValidationResult.failure(
                    ChessException(f"{method}: Domain cannot have a null square list.")
                )
            
            if domain.enemies is None:
                return ValidationResult.failure(
                    ChessException(f"{method}: Domain cannot have a null enemies dictionary.")
                )
            
            if domain.friends is None:
                return ValidationResult.failure(
                    ChessException(f"{method}: Domain cannot have a null friends dictionary.")
                )
            
            return ValidationResult.success(domain)
        
        except Exception as e:
            return ValidationResult.failure(
                InvalidDomainException(f"{method}: {InvalidDomainException.DEFAULT_MESSAGE}", e)
            )
