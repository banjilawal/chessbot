# src/chess/square/context/validator/validator.py

"""
Module: chess.square.context.validator.validator
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import Any, cast

from chess.board import BoardIntegrityService
from chess.coord.service import CoordIntegrityService
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.square import (
    InvalidSquareContextException, NoSquareContextFlagSetException, NullSquareContextException,
    SquareContext, TooManySquareContextFlagsSetException
)


class SquareContextValidator(Validator[SquareContext]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            board_service: BoardIntegrityService = BoardIntegrityService(),
            coord_service: CoordIntegrityService = CoordIntegrityService(),
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[SquareContext]:
        """"""
        method = "SquareContextValidator.validate"
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullSquareContextException(
                        f"{method}: {NullSquareContextException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, SquareContext):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Was expecting a SquareContext, "
                        f"got {type(candidate)} instead."
                    )
                )
            
            context = cast(SquareContext, candidate)
            flag_count = len(context.to_dict())
            
            if flag_count == 0:
                return ValidationResult.failure(
                    NoSquareContextFlagSetException(
                        f"{method}: "
                        f"{NoSquareContextFlagSetException.DEFAULT_MESSAGE}")
                )
            
            if flag_count > 1:
                return ValidationResult.failure(
                    TooManySquareContextFlagsSetException(
                        f"{method}: "
                        f"{TooManySquareContextFlagsSetException.DEFAULT_MESSAGE}"
                    )
                )
            
            if context.id is not None:
                id_validation = identity_service.validate_id(candidate=context.id)
                if id_validation.is_failure:
                    return ValidationResult.failure(id_validation.exception)
                return ValidationResult.success(payload=context)
            
            if context.name is not None:
                name_validation = identity_service.validate_name(context.name)
                if name_validation.is_failure:
                    return ValidationResult.failure(name_validation.exception)
                return ValidationResult.success(payload=context)
            
            if context.coord is not None:
                coord_validation = coord_service.item_validator.validate(context.coord)
                if coord_validation.is_failure:
                    return ValidationResult.failure(coord_validation.exception)
                return ValidationResult.success(payload=context)
            
        except Exception as ex:
            return ValidationResult.failure(
                InvalidSquareContextException(
                    ex=ex,
                    message=f"{method}: "
                            f"{InvalidSquareContextException.DEFAULT_MESSAGE}"
                )
            )