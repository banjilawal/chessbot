# src/operation/bootstrap/validation/binder/operation.py

"""
Module: operation.boostrap.validation.binder.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, cast

from err import BinderNullException, BoardTeamBinderNullException, BoardTeamBinderValidationException, NullException
from microvalidator import SchemaValidator

from err.null.hashtable.exception import HashtableNullException
from model import Binder, BoardBinder, Schema, Team
from operation import ValidationBootstrapper, Validator
from result import ValidationResult
from util import LoggingLevelRouter
from toolkit import BoardTeamBinderToolkit


class SchemaHashtableValidator(Validator[Dict[Schema, Any]]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure the object is a Dict with schemas as its keys.

    Attributes:

    Properties:
        -   def validate(
                candidate: Any,
                schema_validator: SchemaDictValidator,
                validation_bootstrapper: ValidationBootstrapper,
            ) -> ValidationResult[Dict[Schema, Any]]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            schema_validator: SchemaValidator,
            validation_bootstrapper: ValidationBootstrapper,
    ) -> ValidationResult[Binder]:
        """
        Verify the candidate is a BinderTable that.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a BoardTeamBinder.
                    -   The boardTeamBinder's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
            schema_validator: SchemaValidator
            validation_bootstrapper: ValidationBootstrapper
        Returns:
            ValidationResult[Dict[Schema, Any]]
        Raises:
            TypeError
            BoardTeamBinderNullException
            ZeroBoardTeamBinderFlagsException
            BoardTeamBinderValidationException
            ExcessBoardTeamBinderFlagsException
        """
        method = f"{cls.__name__}.validate"
            
        # Handle the case that, the candidate does not exist.
        validation_bootstrap_result = validation_bootstrapper.validate(
            candidate=candidate,
            target_model=Dict[Schema, Any],
            null_exception=HashtableNullException(),
        )
        if validation_bootstrap_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardTeamBinderValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardTeamBinderValidationException.MSG,
                    err_code=BoardTeamBinderValidationException.ERR_CODE,
                    ex=validation_bootstrap_result.exception,
                )
            )
        table = cast(Dict[Schema, Any], validation_bootstrap_result.payload)
        
        for key in table.keys():
            schema_validation_result = schema_validator.validator.validate(table[key])
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardTeamBinderValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BoardTeamBinderValidationException.MSG,
                    err_code=BoardTeamBinderValidationException.ERR_CODE,
                    ex=schema_validation_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(table)
        

    

            