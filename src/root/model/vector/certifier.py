# src/certifier/vector/validator.py

"""
Module: certifier.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from toggle.carrier import VectorCarrier
from model import Vector
from root import RootCertifier
from result import ValidationResult
from toolkit import VectorToolkit
from util import LoggingLevelRouter


class VectorRootCertifier(RootCertifier[Vector]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a VectorBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: VectorToolkit

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        Certifier
    """
    
    def __init__(self, toolkit: VectorToolkit | None = VectorToolkit()):
        """
        Args:
            toolkit: VectorToolkit
        """
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> VectorToolkit:
        return cast(VectorToolkit, super().toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate, Any) -> ValidationResult:
        """
        Certify a candidate is a VectorBlueprint that is safe to use.

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
            ValidationResult
        Raises:
            VectorCertifierException
            VectorDtoCarrierNullException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.model_carrier_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.carrier_model,
            model_null_exception=self.toolkit.carrier_null_exception,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorCertifierException.MSG,
                    err_code=VectorCertifierException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(self.toolkit.carrier_model, carrier_validation.payload)

        # --- Cast the candidate into a VectorBlueprint for additional tests. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that, any id in the blueprint is flagged.
        numbers = []
        for number in [blueprint.x, blueprint.y]:
            validation = self.toolkit.number_validator.execute(number)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    VectorCertifierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCertifierException.MSG,
                        err_code=VectorCertifierException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            numbers.append(cast(int, validation.payload))

        # --- Use the validated numbers to build the appropriate object. ---#
        if carrier.is_model_carrier:
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