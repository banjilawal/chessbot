# src/validator/vector/validator.py

"""
Module: validator.vector.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional, cast

import setting
from err import VectorValidatorException
from model import Vector
from primary import RootCertifier
from result import ValidationResult
from toolkit import VectorToolkit
from util import LoggingLevelRouter
from validator import ModelValidator


class VectorValidator(ModelValidator[Vector]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Vector instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                     toolkit: VectorToolkit
            ) -> ValidationResult[Vector]:

    Super Class:
        Validator
    """
    
    def __init__(self, root_certifier: Optional[RootCertifier[Vector]] | None = None):
        super().__init__(root_certifier=root_certifier)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            toolkit: VectorToolkit | None = None,
    ) -> ValidationResult[Vector]:
        """
        Check if a Vector is safe to use.

        Action:
            1.  Send an exception in the ValidationResult if either x or y
                    -   Is null
                    -   Not a number
                    -   Out of  bounds.
            2.  Otherwise, send the success result.
        Args:
             candidate: Any
             toolkit: VectorToolkit
        Returns:
            ValidationResult[Vector]
        Raises:
            TypeError
            NullVectorException
            VectorValidatorException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply missing dependencies. ---#
        if toolkit is None:
            toolkit = VectorToolkit()
        
        # Handle the case that, the validator is not primed.
        validator_priming_result = toolkit.priming_validator.execute(
            candidate=candidate,
            context_model=toolkit.model,
            context_null_exception=toolkit.null_exception,
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorValidatorException.MSG,
                    err_code=VectorValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast the candidate to a Vector for additional tests ---#
        vector = cast(toolkit.model, candidate)
        
        # Handle the case that, either component is out of bounds.
        for num in [vector.x, vector.y]:
            validation_result = toolkit.number_validator.execute(
                floor=0,
                candidate=abs(num)
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    VectorValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=VectorValidatorException.MSG,
                        err_code=VectorValidatorException.ERR_CODE,
                        ex=validator_priming_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(vector)