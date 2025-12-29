# src/chess/token/validator/validator.py

"""
Module: chess.token.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, cast

from chess.coord import CoordService
from chess.system import IdentityService, LoggingLevelRouter, Validator, ValidationResult
from chess.token import (
)

class TokenContextValidator(Validator[TokenContext]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[TokenContext]:
        """"""
        method = "TokenContextValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTokenContextException(
                        f"{method}: "
                        f"{NullTokenContextException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, TokenContext):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected TokenContext instance, got {type(candidate).__name__} instead."
                    )
                )
            
            context = cast(TokenContext, candidate)
            
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroTokenContextFlagsException(
                        f"{method}: "
                        f"{ZeroTokenContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    ExcessiveTokenContextFlagsException(
                        F"{method}: "
                        F"{ExcessiveTokenContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if context.id is not None:
                validation = identity_service.validate_id(candidate=context.id)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.name is not None:
                validation = identity_service.validate_name(candidate=context.name)
                if validation.is_failure:
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
                InvalidTokenContextException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{InvalidTokenContextException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
    
