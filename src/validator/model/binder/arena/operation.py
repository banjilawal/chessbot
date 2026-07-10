# src/validator/binder/board/__init__.py

"""
Module: validator.binder.board.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, cast

from err import BoardTeamBinderNullException, BoardTeamBinderValidatorException
from model import BoardBinder, Schema, Team
from operation import Validator
from bootstrapper.validator.binder.operation import SchemaHashtableValidator
from result import ValidationResult
from util import LoggingLevelRouter
from toolkit import BoardTeamBinderToolkit


class BoardTeamBinderValidator(ModelValidator[BoardBinder]):
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
        ModelValidator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: BoardTeamBinderToolkit,
    ) -> ValidationResult[BoardBinder]:
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
            BoardTeamBinderValidatorException
            ExcessBoardTeamBinderFlagsException
        """
        method = f"{self.__class__.__name__}.execute"
        
        if toolkit is None:
            toolkit = BoardTeamBinderToolkit()
            
        # Handle the case that, the validator is not primed.
        validator_priming_result = toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=BoardBinder,
            null_exception=BoardTeamBinderNullException(),
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardTeamBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderValidatorException.MSG,
                    err_code=BoardTeamBinderValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        binder = validator_priming_result.payload
        board_validator_result =toolkit.board_service.run.build(binder.primary)
        
        if board_validator_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardTeamBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderValidatorException.MSG,
                    err_code=BoardTeamBinderValidatorException.ERR_CODE,
                    ex=board_validator_result.exception,
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(binder)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_satellite_table_checks(
            cls,
            binder: BoardBinder,
            toolkit: BoardTeamBinderToolkit
    ) -> ValidationResult[Dict[Schema, Team]]:
        method = f"{self.__class__.__name__}.run_satellite_table_checks"
        
        # Handle the case that, the satellite is not a dictionary or null.
        table_validation_result = SchemaHashtableValidator.execute(binder)
        if table_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardTeamBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderValidatorException.MSG,
                    err_code=BoardTeamBinderValidatorException.ERR_CODE,
                    ex=table_validation_result.exception
                )
            )
        # --- Cast to Dict for additional tests. ---#
        table = cast(Dict[Schema, Any], table_validation_result.payload)
        
        # handle the case that, the keys are not safe schemas.
        for key in table.keys():
            schema_validation_result = toolkit.schema_service.validator.execute(table[key])
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardTeamBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderValidatorException.MSG,
                    err_code=BoardTeamBinderValidatorException.ERR_CODE,
                    ex=schema_validation_result.exception
                )
            )
        # Handle the case that, the values are not safe teams.
        for key in table.keys():
            team_validation_result = toolkit.schema_service.validator.execute(table[key])
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardTeamBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardTeamBinderValidatorException.MSG,
                    err_code=BoardTeamBinderValidatorException.ERR_CODE,
                    ex=team_validation_result.exception
                )
            )
        # --- Return the work product to the caller. ---#
        return ValidationResult.success(table)