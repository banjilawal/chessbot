# src/assurance/validator/root/space/quadrant/northwest/assurance/checker.py

"""
Module: assurance.validator.space.quadrant.northwest.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, cast

from domain.metadata.blueprint import NorthwestQuadrantBlueprint
from carrier import NorthwestQuadrantCarrier
from err import NorthwestQuadrantCarrierNullException, NorthwestQuadrantRootCheckerException
from domain.model import Vector
from artifcat import ValidationResult
from assurance.validator import QuadrantRootChecker
from space import NorthwestQuadrant
from operation.toolkit.geometry.space.quadrant import NorthwestQuadrantToolkit
from util import LoggingLevelRouter


class NorthwestQuadrantRootChecker(QuadrantRootChecker[NorthwestQuadrantBlueprint]):
    """
    Role
        -  Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a NorthwestQuadrantBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        bundle: NorthwestQuadrantToolkit

    Provides:
        -  execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        IntegrityChecker
    """
    
    def __init__(self, bundle: NorthwestQuadrantToolkit | None = NorthwestQuadrantToolkit()):
        """
        Args:
            bundle: NorthwestQuadrantToolkit
        """
        super().__init__(bundle=bundle)
    
    @property
    def toolkit(self) -> NorthwestQuadrantBundle:
        return cast(NorthwestQuadrantToolkit, super().ruleset)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[NorthwestQuadrant| NorthwestQuadrantBlueprint]:
        """
        Certify a candidate is a NorthwestQuadrantBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -  The validation_priming fails.
                    -  Either the board, owner or id get flagged unsafe.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
        Returns:
            ValidationResult
        Raises:
            NorthwestQuadrantRootCheckerException
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
                NorthwestQuadrantRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NorthwestQuadrantRootCheckerException.MSG,
                    err_code=NorthwestQuadrantRootCheckerException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(NorthwestQuadrantCarrier, carrier_validation.payload)
        if carrier.is_not_carrying_anything:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NorthwestQuadrantRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NorthwestQuadrantRootCheckerException.MSG,
                    err_code=NorthwestQuadrantRootCheckerException.ERR_CODE,
                    ex=NorthwestQuadrantCarrierNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NorthwestQuadrantCarrierNullException.MSG,
                        err_code=NorthwestQuadrantCarrierNullException.ERR_CODE,
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
                    NorthwestQuadrantRootCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NorthwestQuadrantRootCheckerException.MSG,
                        err_code=NorthwestQuadrantRootCheckerException.ERR_CODE,
                        ex=vector_validation.exception,
                    )
                )
            vectors.append(cast(Vector, vector_validation.payload))
        # --- Extract and cast payloads of the validation results. ---#
        origin = vectors[0]

        if carrier.is_carrying_model:
            return ValidationResult.success(
                NorthwestQuadrant(origin=origin)
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            NorthwestQuadrantBlueprint(origin=origin)
        )