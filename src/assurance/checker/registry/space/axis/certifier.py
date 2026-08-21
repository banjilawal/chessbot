# src/root/space/reservoir/axis/assurance/checker.py

"""
Module: root.space.reservoir.axis.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.blueprint import AxisReservoirBlueprint
from carrier import AxisReservoirCarrier
from domain.model import Vector
from assurance.checker import SpaceReservoirChecker
from result import ValidationResult
from space import AxisReservoir
from toolkit import AxisReservoirToolkit
from util import LoggingLevelRouter


class AxisReservoirRootChecker(SpaceReservoirChecker[AxisReservoir]):
    """
    Role
        -   Validator
        -   Integrity Assurance
        -   Consistency Assurance

    Responsibilities:
        1.  Runs integrity checks on Spaces and SpaceBlueprints before they are used.
        2.  Pluggable validation module.

    Attributes:
        bundle: SpaceToolkit

    Provides:
        -   def execute(candidate: Any, bundle: SpaceToolkit,) -> ValidationResult[Blueprint[T]]:

    Super Class:
    """

    def __init__(self, bundle: Optional[AxisReservoirToolkit] | None = None):
        super().__init__(bundle=bundle or AxisReservoirToolkit())
        
    @property
    def toolkit(self) -> AxisReservoirBundle:
        return cast(AxisReservoirToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate, Any) -> ValidationResult[AxisReservoir|AxisReservoirBlueprint]:
        """
        Certify a candidate is a AxisReservoir or its Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate is not a AxisReservoirDtoCarrier.
                    -   The candidate is an empty AxisReservoirDtoCarrier.
                    -   Either the board, team, formation, rank or id get flagged unsafe.
            2.  For a model_carrier send a AxisReservoir in the success result. Otherwise, send 
                the AxisReservoirBlueprint.
        Args:
            candidate, Any
        Returns:
            ValidationResult
        Raises:
            AxisReservoirCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.carrier_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.carrier_model,
            model_null_exception=self.toolkit.carrier_null_exception,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AxisReservoirRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisReservoirRootCheckerException.MSG,
                    err_code=AxisReservoirRootCheckerException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(AxisReservoirCarrier, carrier_validation.payload)
        
        # --- Cast the candidate into a AxisReservoirBlueprint for additional tests. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that, the origin is flagged unsafe.
        validation = self.toolkit.math.vector.validator.execute(blueprint.origin)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AxisReservoirRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisReservoirRootCheckerException.MSG,
                    err_code=AxisReservoirRootCheckerException.ERR_CODE,
                    ex=validation.exception
                )
            )
        origin = cast(Vector, validation.payload)
        if carrier.is_carrying_model:
            return ValidationResult.success(
                AxisReservoirCarrier(model=AxisReservoir(origin=origin))
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            AxisReservoirCarrier(blueprint=AxisReservoirBlueprint(origin=origin))
        )
    
    
