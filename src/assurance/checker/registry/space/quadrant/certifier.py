# src/root/space/reservoir/quadrant/assurance/checker.py

"""
Module: root.space.reservoir.quadrant.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import QuadrantReservoirBlueprint
from carrier import QuadrantReservoirCarrier
from domain.model import Vector
from assurance.checker import SpaceReservoirChecker
from result import ValidationResult
from space import QuadrantReservoir
from operation.toolkit import QuadrantReservoirToolkit
from util import LoggingLevelRouter


class QuadrantReservoirRootChecker(SpaceReservoirChecker[QuadrantReservoir]):
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

    def __init__(self, bundle: Optional[QuadrantReservoirToolkit] | None = None):
        super().__init__(bundle=bundle or QuadrantReservoirToolkit())
        
    @property
    def toolkit(self) -> QuadrantReservoirBundle:
        return cast(QuadrantReservoirToolkit, super().ruleset)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate, Any) -> ValidationResult[QuadrantReservoir|QuadrantReservoirBlueprint]:
        """
        Certify a candidate is a QuadrantReservoir or its Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate is not a QuadrantReservoirDtoCarrier.
                    -   The candidate is an empty QuadrantReservoirDtoCarrier.
                    -   Either the board, team, formation, rank or id get flagged unsafe.
            2.  For a model_carrier send a QuadrantReservoir in the success result. Otherwise, send 
                the QuadrantReservoirBlueprint.
        Args:
            candidate, Any
        Returns:
            ValidationResult
        Raises:
            QuadrantReservoirCheckerException
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
                QuadrantReservoirRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantReservoirRootCheckerException.MSG,
                    err_code=QuadrantReservoirRootCheckerException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(QuadrantReservoirCarrier, carrier_validation.payload)
        
        # --- Cast the candidate into a QuadrantReservoirBlueprint for additional tests. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that, the origin is flagged unsafe.
        validation = self.toolkit.math.vector.validator.execute(blueprint.origin)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                QuadrantReservoirRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantReservoirRootCheckerException.MSG,
                    err_code=QuadrantReservoirRootCheckerException.ERR_CODE,
                    ex=validation.exception
                )
            )
        origin = cast(Vector, validation.payload)
        if carrier.is_carrying_model:
            return ValidationResult.success(
                QuadrantReservoirCarrier(model=QuadrantReservoir(origin=origin))
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            QuadrantReservoirCarrier(blueprint=QuadrantReservoirBlueprint(origin=origin))
        )
    
    
