# src/operation/validation/context/board/__ini__.py

"""
Module: operation.validation.context.board.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any

from model import BoardTeamBinder
from operation import Validator
from system import LoggingLevelRouter


class BoardContextValidator(Validator[BoardTeamBinder]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a BoardContext instance is certified safe, reliable and consistent
            before use.

    Attributes:

    Properties:
        -   def validate(
                    candidate: Any,
                    toolkit : BoardContextToolSe,
            ) -> ValidationResult[BoardContext]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: BoardTeamBinderToolkit,
    ) -> ValidationResult[BoardTeamBinder]:
        """
        Verify the candidate is a safe BoardContext.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a BoardContext.
                    -   The boardContext's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
            toolkit : BoardContextToolkit
        Returns:
            ValidationResult[BoardContext]
        Raises:
            TypeError
            BoardContextNullException
            ZeroBoardContextFlagsException
            BoardContextValidationException
            ExcessBoardContextFlagsException
        """
        method = f"{cls.__name__}.validate"
        
        if toolkit is None:
            toolkit = BoardContextToolkit()
            
        # Handle the case that, the candidate does not exist.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardContextValidationException.MSG,
                    err_code=BoardContextValidationException.ERR_CODE,
                    ex=BoardContextNullException(
                        msg=BoardContextNullException.MSG,
                        err_code=BoardContextNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the candidate is wrong type.
        if not isinstance(candidate, BoardTeamBinder):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardContextValidationException.MSG,
                    err_code=BoardContextValidationException.ERR_CODE,
                    ex=TypeError(
                        f"Expected Board type, got ({candidate}.__name__) instead."
                    )
                )
            )
        # --- Cast candidate to a BoardContext for additional tests. ---#
        context = cast(BoardTeamBinder, candidate)
        
        # Handle the case that neither option is enabled.
        if len(context.to_dict) == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardContextValidationException.MSG,
                    err_code=BoardContextValidationException.ERR_CODE,
                    ex=ZeroBoardContextFlagsException(
                        msg=ZeroBoardContextFlagsException.MSG,
                        err_code=ZeroBoardContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, both options are enabled.
        if len(context.to_dict) > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardContextValidationException.MSG,
                    err_code=BoardContextValidationException.ERR_CODE,
                    ex=ExcessBoardContextFlagsException(
                        msg=ExcessBoardContextFlagsException.MSG,
                        err_code=ExcessBoardContextFlagsException.ERR_CODE,
                    )
                )
            )
        # --- Assign to the correct service for the final step. ---#
        validation_result = None
        if isinstance(context.board, Board):
            validation_result = toolkit.board_service.validator.validate(context.board)
        if isinstance(context.coord, Coord):
            validation_result = toolkit.coord_service.validator.validate(context.to_dict)
            
        # Handle the case that context was flagged.
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardContextValidationException.MSG,
                    err_code=BoardContextValidationException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(context)

            