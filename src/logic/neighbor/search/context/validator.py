# src/logic/neighbor/searcher/exception.py

"""
Module: logic.neighbor.searcher.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-05
version: 1.0.0
"""

from typing import cast, TypeVar

from logic.coord import CoordValidator
from logic.rank import Bishop, King, Knight, Pawn, Queen, Rank, RankSpec, Rook
from system import IdValidator, LoggingLevelRouter, NameValidator, Validator, ValidationResult
from logic.piece import (
    DomainContext, InvalidDomainContextException, NullDomainContextException,
    ArenaDomainSearchParamsException, ZeroDomainSearchParamsException, DomainInvalidRankNameParamException
)


class DomainContextValidator(Validator[DomainContext]):
    """
     Role:Validation, Data Integrity Guarantor, Security., Data Integrity
  
    Responsibilities:
    1. Process and validate parameters for creating `DomainContext` instances.
    2. Create new `DomainContext` objects if parameters meet specifications.
    2. Report errors and return `BuildResult` with error details.
  
    # PROVIDES:
    `BuildResult`: Return type containing the built `DomainContext` or error information.
  
    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: T) -> ValidationResult[DomainContext]:
        """"""
        method = "DomainContextValidator.execute"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullDomainContextException(f"{method} {NullDomainContextException.MSG}")
                )
            
            if not isinstance(candidate, DomainContext):
                return ValidationResult.failure(
                    TypeError(
                        f"{method} Expected domainContext DomainContext, got {type(candidate).__name__}"
                        )
                )
            
            search_context = cast(DomainContext, candidate)
            
            if len(search_context.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroDomainSearchParamsException(f"{method} {ZeroDomainSearchParamsException.MSG}")
                )
            
            if len(search_context.to_dict()) > 1:
                return ValidationResult.failure(
                    ArenaDomainSearchParamsException(
                        f"{method} {InvalidDomainContextException.MSG}"
                        )
                )
            
            if search_context.piece_id is not None:
                piece_id_validation = Idvalidator.execute(search_context.piece_id)
                if piece_id_validation.is_failure():
                    return ValidationResult.failure(piece_id_validation.exception)
            
            if search_context.visitor_name is not None:
                piece_name_validation = Namevalidator.execute(search_context.visitor_name)
                if piece_name_validation.is_failure():
                    return ValidationResult.failure(piece_name_validation.exception)
            
            if search_context.team_id is not None:
                team_id_validation = Idvalidator.execute(search_context.team_id)
                if team_id_validation.is_failure():
                    return ValidationResult.failure(team_id_validation.exception)
            
            if search_context.visitor_team is not None:
                team_name_validation = Namevalidator.execute(search_context.visitor_team)
                if team_name_validation.is_failure():
                    return ValidationResult.failure(team_name_validation.exception)
            
            if search_context.visitor_rank is not None and search_context.visitor_rank.upper() not in Persona.__members__:
                return ValidationResult.failure(
                    DomainInvalidRankNameParamException(
                        f"{method}: {DomainInvalidRankNameParamException.MSG}"
                        )
                )
            
            if search_context.visitor_ransom not in range[Queen.ransom]:
                return ValidationResult.failure(
                    DomainInvalidRankNameParamException(
                        f"{method}: {DomainInvalidRankNameParamException.MSG}"
                        )
                )
            
            if search_context.position is not None:
                position_validation = Coordvalidator.execute(search_context.position)
                if position_validation.is_failure():
                    return ValidationResult.failure(position_validation.exception)
            
            return ValidationResult.success(search_context)
        
        except Exception as e:
            return ValidationResult.failure(e)
