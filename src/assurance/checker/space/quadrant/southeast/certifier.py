# src/assurance/checker/root/space/quadrant/southeast/assurance/checker.py

"""
Module: assurance.checker.space.quadrant.southeast.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, cast

from domain.metadata.blueprint import SoutheastQuadrantBlueprint
from carrier import SoutheastQuadrantCarrier
from domain.model import Vector
from result import ValidationResult
from assurance.checker import QuadrantRootChecker
from space import SoutheastQuadrant
from toolkit.geometry.space.quadrant import SoutheastQuadrantToolkit
from util import LoggingLevelRouter


class SoutheastQuadrantRootChecker(QuadrantRootChecker[SoutheastQuadrantBlueprint]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a SoutheastQuadrantBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        bundle: SoutheastQuadrantToolkit

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        IntegrityChecker
    """
    
    def __init__(self, bundle: SoutheastQuadrantToolkit | None = SoutheastQuadrantToolkit()):
        """
        Args:
            bundle: SoutheastQuadrantToolkit
        """
        super().__init__(bundle=bundle)
    
    @property
    def toolkit(self) -> SoutheastQuadrantBundle:
        return cast(SoutheastQuadrantToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[SoutheastQuadrant| SoutheastQuadrantBlueprint]:
        """
        Certify a candidate is a SoutheastQuadrantBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The validation_priming fails.
                    -   Either the board, owner or id get flagged unsafe.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
        Returns:
            ValidationResult
        Raises:
            SoutheastQuadrantRootCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.carrier_model,
            null_exception=self.toolkit.carrier_null_exception,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SoutheastQuadrantRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SoutheastQuadrantRootCheckerException.MSG,
                    err_code=SoutheastQuadrantRootCheckerException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(SoutheastQuadrantCarrier, carrier_validation.payload)
        if carrier.is_not_carrying_anything:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SoutheastQuadrantRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SoutheastQuadrantRootCheckerException.MSG,
                    err_code=SoutheastQuadrantRootCheckerException.ERR_CODE,
                    ex=SoutheastQuadrantCarrierNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SoutheastQuadrantCarrierNullException.MSG,
                        err_code=SoutheastQuadrantCarrierNullException.ERR_CODE,
                    ),
                )
            )
        # --- Cast the candidate into a TokenBlueprint for additional tests. ---#
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that, any id in the blueprint is flagged.
        vectors: List[Vector] = []
        for vector in [blueprint.origin, blueprint.terminus]:
            vector_validation = self.toolkit.math.vector.validator.execute(
                candidate=vector,
            )
            if vector_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SoutheastQuadrantRootCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SoutheastQuadrantRootCheckerException.MSG,
                        err_code=SoutheastQuadrantRootCheckerException.ERR_CODE,
                        ex=vector_validation.exception,
                    )
                )
            vectors.append(cast(Vector, vector_validation.payload))
        # --- Extract and cast payloads of the validation results. ---#
        origin = vectors[0]
        terminus = None
        if len(vectors) == 2:
            terminus = vectors[1]

        if carrier.is_carrying_model:
            return ValidationResult.success(
                SoutheastQuadrant(origin=origin)
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            SoutheastQuadrantBlueprint(origin=origin)
        )