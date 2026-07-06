# src/validator/schema/validator.py

"""
Module: validator.schema.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any

from model import Schema
from operation import Validator
from result import ValidationResult
from util import LoggingLevelRouter


class SchemaValidator(Validator[Schema]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Archetype instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(candidate: Any) -> ValidationResult[Archetype]

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Schema]:
        """
        Verify the Archetype is safe before its used.
        
        Action:
            1.  Send the exception chain in the ValidationResult if either:
                    -   The candidate is null.
                    -   It's not a Archetype.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Archetype]
        Raises:
            TypeError
            NullSchemaException
            SchemaValidationException
        """
        method = f"{cls.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=SchemaValidationException.OP,
                    msg=SchemaValidationException.MSG,
                    err_code=SchemaValidationException.ERR_CODE,
                    mthd_rslt_type=SchemaValidationException.MTHD_RSLT,
                    ex=NullSchemaException(
                        msg=SchemaValidationException.MSG,
                        err_code=SchemaValidationException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Schema):
            # Return the exception chain on failure
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=SchemaValidationException.OP,
                    msg=SchemaValidationException.MSG,
                    err_code=SchemaValidationException.ERR_CODE,
                    mthd_rslt_type=SchemaValidationException.MTHD_RSLT,
                    ex=TypeError(
                        f"Expected a Archetype, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(cast(Schema, candidate))