# src/validation/vector/validator.py

"""
Module: validation.vector.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from controller import WorkerRegistryController
from model import Vector
from toolkit import MathToolkit
from operation import Validator
from result import ValidationResult
from system import BOARD_DIMENSION, LoggingLevelRouter
from err import VectorNullException, VectorValidationException




class VectorValidator(Validator[Vector]):
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
                     toolkit: MathToolkit
            ) -> ValidationResult[Vector]:

    Super Class:
        Validator
    """
    OPERATION_NAME = "vector_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: MathToolkit | None = None
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
             toolkit: MathToolkit
        Returns:
            ValidationResult[Vector]
        Raises:
            TypeError
            NullVectorException
            VectorValidationException
        """
        method = f"{cls.__name__}.validate"
        
        if toolkit is None:
            toolkit = MathToolkit()
        
        # Handle the case that, the candidate does not exist.
        validation_priming_result = toolkit.validation_primer.execute(
            candidate=candidate,
            target_model=Vector,
            context_null_exception=VectorNullException(),
        )
        if validation_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorValidationException.MSG,
                    err_code=VectorValidationException.ERR_CODE,
                    ex=validation_priming_result.exception,
                )
            )
        # --- Cast the candidate to a Vector for additional tests ---#
        vector = cast(Vector, candidate)
        
        # Handle the case that, either component is out of bounds.
        for num in [vector.x, vector.y]:
            validation_result = toolkit.number_validator.validate(
                floor=0,
                ceiling=BOARD_DIMENSION - 1,
                candidate=abs(num)
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    VectorValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=VectorValidationException.MSG,
                        err_code=VectorValidationException.ERR_CODE,
                        ex=validation_priming_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(vector)

# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=VectorValidator)