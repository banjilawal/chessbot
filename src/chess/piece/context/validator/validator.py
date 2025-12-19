# src/chess/piece/context/validator/validator.py

"""
Module: chess.piece.context.validator.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, cast

from chess.coord import CoordService
from chess.system import IdentityService, LoggingLevelRouter, Validator, ValidationResult
from chess.piece import (
    InvalidPieceContextException, ZeroPieceContextFlagsException, NullPieceContextException, PieceContext,
    ExcessivePieceContextFlagsSetException
)

class PieceContextValidator(Validator[PieceContext]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            coord_service: CoordService = CoordService(),
            idservice: IdentityService = IdentityService(),
    ) -> ValidationResult[PieceContext]:
        """"""
        method = "PieceContextValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullPieceContextException(
                        f"{method}: "
                        f"{NullPieceContextException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, PieceContext):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected PieceContext, got {type(candidate).__name__} instead."
                    )
                )
            
            context = cast(PieceContext, candidate)
            
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroPieceContextFlagsException(
                        f"{method}: "
                        f"{ZeroPieceContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    ExcessivePieceContextFlagsSetException(
                        F"{method}: "
                        F"{ExcessivePieceContextFlagsSetException.DEFAULT_MESSAGE}"
                    )
                )
            
            if context.id is not None:
                validation = idservice.validate_id(candidate=context.id)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.name is not None:
                validation = idservice.validate_name(candidate=context.name)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.coord is not None:
                validation = coord_service.item_validator.validate(
                    candidate=candidate,
                    validator=coord_service.item_validator
                )
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.succes(context)
                
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPieceContextException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{InvalidPieceContextException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
    
