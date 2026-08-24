# src/assurance/checker/model/vector/checker.py

"""
Module: assurance.checker.model.vector.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from assurance import ModelIntegrityChecker, VectorValidationBundle
from domain import Vector, VectorBlueprint, VectorCarrier
from err import VectorIntegrityCheckerException
from artifcat import ValidationResult
from util import LoggingLevelRouter


class VectorIntegrityChecker(ModelIntegrityChecker[Vector]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a VectorBlueprint instance is certified safe, reliable, and consistent before use.

    Attributes:
        bundle: Optional[VectorValidationToolkit]

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult[Vector|VectorBlueprint]:

    Super Class:
        IntegrityChecker
    """
    
    def __init__(self, bundle: Optional[VectorValidationBundle] | None = None):
        """
        Args:
            bundle: Optional[VectorValidationToolkit]
        """
        super().__init__(bundle=bundle or VectorValidationBundle())
        
    @property
    def bundle(self) -> VectorValidationBundle:
        return cast(VectorValidationBundle, super().bundle)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any)-> ValidationResult[Vector|VectorBlueprint]:
        """
        Certify a candidate is either a Vector or its Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate is not a VectorDtoCarrier.
                    -   The candidate is an empty VectorDtoCarrier.
                    -   Either the board, team, formation, rank or id get flagged unsafe.
            2.  For a model_carrier send a Vector in the success result. Otherwise, send a TokeBlueprint.
        Args:
            candidate, Any
        Returns:
            ValidationResult[Vector|VectorBlueprint]
        Raises:
            VectorIntegrityCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.bundle.priming_validator.execute(
            candidate=candidate,
            target_model=self.bundle.types.carrier,
            null_exception=self.bundle.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorIntegrityCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorIntegrityCheckerException.MSG,
                    err_code=VectorIntegrityCheckerException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(self.bundle.types.carrier, carrier_validation.payload)

        # --- Cast the candidate into a VectorBlueprint for additional tests. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that, any id in the blueprint is flagged.
        numbers = []
        for number in [blueprint.x, blueprint.y]:
            validation = self.bundle.number_validator.execute(number)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    VectorIntegrityCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorIntegrityCheckerException.MSG,
                        err_code=VectorIntegrityCheckerException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            numbers.append(cast(int, validation.payload))

        # --- Use the validated numbers to build the appropriate object. ---#
        if carrier.is_carrying_model:
            return ValidationResult.success(
                VectorCarrier(model=Vector(x=numbers[0], y=numbers[1])))
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            VectorCarrier(blueprint=VectorBlueprint(x=numbers[0], y=numbers[1]))
        )