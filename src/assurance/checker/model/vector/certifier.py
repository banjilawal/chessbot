# src/assurance/certifier/vector/validator.py

"""
Module: assurance.certifier.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelChecker, VectorValidationBundle
from fabrication.blueprint import VectorBlueprint
from err import VectorRootCertifierException
from model import Vector
from result import ValidationResult
from transit import VectorCarrier
from util import LoggingLevelRouter


class VectorChecker(ModelChecker[Vector]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a VectorBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: Optional[VectorValidationToolkit]

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult[Vector|VectorBlueprint]:

    Super Class:
        Certifier
    """
    
    def __init__(self, toolkit: Optional[VectorValidationBundle] | None = None):
        """
        Args:
            toolkit: Optional[VectorValidationToolkit]
        """
        super().__init__(toolkit=toolkit or VectorValidationBundle())
        
    @property
    def toolkit(self) -> VectorValidationBundle:
        return cast(VectorValidationBundle, super().toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate, Any) -> ValidationResult[Vector|VectorBlueprint]:
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
            VectorRootCertifierException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.types.carrier,
            model_null_exception=self.toolkit.null_exceptions.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRootCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRootCertifierException.MSG,
                    err_code=VectorRootCertifierException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(self.toolkit.types.carrier, carrier_validation.payload)

        # --- Cast the candidate into a VectorBlueprint for additional tests. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that, any id in the blueprint is flagged.
        numbers = []
        for number in [blueprint.x, blueprint.y]:
            validation = self.toolkit.number_validator.execute(number)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    VectorRootCertifierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorRootCertifierException.MSG,
                        err_code=VectorRootCertifierException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            numbers.append(cast(int, validation.payload))

        # --- Use the validated numbers to build the appropriate object. ---#
        if carrier.is_carrying_model:
            return ValidationResult.success(
                VectorCarrier(
                    model=Vector(
                        x=numbers[0],
                        y=numbers[1]
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            VectorCarrier(
                blueprint=VectorBlueprint(
                    x=numbers[0],
                    y=numbers[1]
                )
            )
        )