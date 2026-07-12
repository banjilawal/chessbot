# src/bootstrap/validator/binder/validator.py

"""
Module: boostrap.validator.binder.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, cast

from err import (
    SchemaHashtableValidatorException
)
from microvalidator import SchemaValidator

from err.null.hashtable import HashtableNullException
from model import Binder, Schema
from operation import PrimingValidator, Validator
from result import ValidationResult
from util import LoggingLevelRouter


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
                priming_validator: PrimingValidator,
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
            priming_validator: PrimingValidator,
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
            priming_validator: PrimingValidator
        Returns:
            ValidationResult[Dict[Schema, Any]]
        Raises:
            SchemaHashtableValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
            
        # Handle the case that, the validator is not primed.
        validator_priming_result = priming_validator.execute(
            candidate=candidate,
            target_model=Dict[Schema, Any],
            context_null_exception=HashtableNullException(),
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaHashtableValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SchemaHashtableValidatorException.MSG,
                    err_code=SchemaHashtableValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        table = cast(Dict[Schema, Any], validator_priming_result.payload)
        
        for key in table.keys():
            schema_validation_result = schema_validator.execute.build(table[key])
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaHashtableValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SchemaHashtableValidatorException.MSG,
                    err_code=SchemaHashtableValidatorException.ERR_CODE,
                    ex=schema_validation_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(table)
        

    

            