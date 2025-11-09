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
from chess.system import ChessException, IdValidator, LoggingLevelRouter, Validator, ValidationResult
from chess.domain import (
    Domain, NullDomainException, InconsistenDomainAddressException, PieceNotOnRosterDomainOwnerException,
    CapturedDomainOwnerException, CheckmatedKingDomainOwnerException,DomainMissingTreeException,
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
            
            owner_validation = PieceValidator.validate(domain.owner)
            if owner_validation.is_failure():
                return ValidationResult.failure(owner_validation.exception)
            
            if isinstance(domain.owner, CombatantPiece) and cast(CombatantPiece, domain.owner).captor is not None:
                return ValidationResult.failure(
                    CapturedDomainOwnerException(f"{method}: {CapturedDomainOwnerException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(domain.owner, KingPiece) and cast(KingPiece, domain.owner).is_checkmated:
                return ValidationResult.failure(
                    CheckmatedKingDomainOwnerException(f"{method}: {CheckmatedKingDomainOwnerException.DEFAULT_MESSAGE}")
                )
            
            team = domain.owner.team
            if domain.owner not in team.roster:
                return ValidationResult.failure(
                    PieceNotOnRosterDomainOwnerException(
                        f"{method}; {PieceNotOnRosterDomainOwnerException.DEFAULT_MESSAGE}"
                    )
                )
            
            if domain.owner.current_position is None:
                return ValidationResult.failure(
                    ChessException(f"{method}: Cannot get the owner of a piece not on the board")
                )
            
            if domain.owner.current_position != domain.owner_address:
                return ValidationResult.failure(
                    InconsistenDomainAddressException(f"{method}: {InconsistenDomainAddressException.DEFAULT_MESSAGE}")
                )
            
            if domain.tree is None:
                return ValidationResult.failure(
                    DomainMissingTreeException(f"{method}: {DomainMissingTreeException.DEFAULT_MESSAGE}")
                )
            
            if domain.owner.current_position not in domain.tree:
                return ValidationResult.failure(
                    ChessException(f"{method}: Owner's current position must be in the tree.")
                )
            
            return ValidationResult.success(domain)
        except Exception as e:
            return ValidationResult.failure(e)
