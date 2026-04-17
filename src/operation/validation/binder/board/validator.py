# src/operation/validation/context/board/__ini__.py

"""
Module: operation.validation.context.board.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any

from err import BoardTeamBinderNullException, BoardTeamBinderValidationException
from model import BoardTeamBinder
from operation import Validator
from result import ValidationResult
from system import LoggingLevelRouter
from toolkit import BoardTeamBinderToolkit


class BoardTeamBinderValidator(Validator[BoardTeamBinder]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a BoardTeamBinder instance is certified safe, reliable and consistent
            before use.

    Attributes:

    Properties:
        -   def validate(
                    candidate: Any,
                    toolkit : BoardTeamBinderToolSe,
            ) -> ValidationResult[BoardTeamBinder]:

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
        Verify the candidate is a safe BoardTeamBinder.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a BoardTeamBinder.
                    -   The boardTeamBinder's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
            toolkit : BoardTeamBinderToolkit
        Returns:
            ValidationResult[BoardTeamBinder]
        Raises:
            TypeError
            BoardTeamBinderNullException
            ZeroBoardTeamBinderFlagsException
            BoardTeamBinderValidationException
            ExcessBoardTeamBinderFlagsException
        """
        method = f"{cls.__name__}.validate"
        
        if toolkit is None:
            toolkit = BoardTeamBinderToolkit()
            
        # Handle the case that, the candidate does not exist.
        validation_bootstrap_result = toolkit.validation_bootstrapper.validate(
            candidate=candidate,
            target_model=BoardTeamBinder,
            null_exception=BoardTeamBinderNullException(),
        )
        if validation_bootstrap_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardTeamBinderValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardTeamBinderValidationException.MSG,
                    err_code=BoardTeamBinderValidationException.ERR_CODE,
                    ex=validation_bootstrap_result.exception,
                )
            )
        binder = validation_bootstrap_result.payload
        board_validation_result =toolkit.board_service.validator.validate(binder.primary)
        if board_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardTeamBinderValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardTeamBinderValidationException.MSG,
                    err_code=BoardTeamBinderValidationException.ERR_CODE,
                    ex=board_validation_result.exception,
                )
            )
            
        
        # Handle the case that neither option is enabled.
        if len(context.to_dict) == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardTeamBinderValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardTeamBinderValidationException.MSG,
                    err_code=BoardTeamBinderValidationException.ERR_CODE,
                    ex=ZeroBoardTeamBinderFlagsException(
                        msg=ZeroBoardTeamBinderFlagsException.MSG,
                        err_code=ZeroBoardTeamBinderFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, both options are enabled.
        if len(context.to_dict) > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BoardTeamBinderValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardTeamBinderValidationException.MSG,
                    err_code=BoardTeamBinderValidationException.ERR_CODE,
                    ex=ExcessBoardTeamBinderFlagsException(
                        msg=ExcessBoardTeamBinderFlagsException.MSG,
                        err_code=ExcessBoardTeamBinderFlagsException.ERR_CODE,
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
                BoardTeamBinderValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardTeamBinderValidationException.MSG,
                    err_code=BoardTeamBinderValidationException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(context)

            