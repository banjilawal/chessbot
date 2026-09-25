# src/transit/dispatcher/validator/model/vector/validator.py

"""
Module: transit.dispatcher.validator.model.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import VectorValidator
from domain.model import Vector
from artifcat import ValidationResult
from transit import ModelValidationDispatcher, VectorCarrier
from util import LoggingLevelRouter



class VectorValidationDispatcher(ModelValidationDispatcher[Vector]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Vector instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: VectorValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[Vector]

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            validator: VectorValidator | None = None,
    ):
        super().__init__(validator=validator or VectorValidator())
        
    @property
    def validator(self) -> VectorValidator:
        return cast(VectorValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[VectorCarrier]:
        """
        Verify the object is a Vector that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test.
            2.  Otherwise, cast the payload into a Vector and send in the success result.
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Vector]
        Raises:
             VectorValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(candidate)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationDispatcherException.MSG,
                    err_code=VectorValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(VectorCarrier, validation.payload)
        return ValidationResult.success(carrier)