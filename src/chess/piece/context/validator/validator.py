# src/chess/piece/context/validator/validator.py

"""
Module: chess.piece.context.validator.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from typing import Any, cast

from chess.coord import CoordService
from chess.piece import (
    InvalidPieceContextException, NoPieceContextFlagSetException, NullPieceContextException,
    NullPieceException, Piece, PieceContext, TooManyPieceContextFlagsSetException
)
from chess.system import IdentityService, LoggingLevelRouter, Validator, ValidationResult


class PieceContextValidator(Validator[Piece]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
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
                        f"{method}: Expected PieceContext, got {type(candidate)} instead."
                    )
                )
            
            context = cast(PieceContext, candidate)
            
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoPieceContextFlagSetException(
                        f"{method}: "
                        f"{NoPieceContextFlagSetException.DEFAULT_MESSAGE}"
                    )
                )
            
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    TooManyPieceContextFlagsSetException(
                        F"{method}: "
                        F"{TooManyPieceContextFlagsSetException.DEFAULT_MESSAGE}"
                    )
                )
            
            if context.id is not None:
                id_validation = identity_service.validate_id(context.id)
                if id_validation.is_failure():
                    return ValidationResult.failure(id_validation.exception)
                return ValidationResult.success(context)
            
            if context.name is not None:
                name_validation = identity_service.validate_name(context.name)
                if name_validation.is_failure():
                    return ValidationResult.failure(name_validation.exception)
                return ValidationResult.success(context)
            
            if context.coord is not None:
                coord_validation = coord_service.validator.validate(
                    candidate=candidate,
                    validator=coord_service.validator
                )
                if coord_validation.is_failure():
                    return ValidationResult.failure(
                        coord_validation.exception
                    )
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
        
    
