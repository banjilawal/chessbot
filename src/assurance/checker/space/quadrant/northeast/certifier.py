# src/assurance/checker/root/space/quadrant/northeast/assurance/checker.py

"""
Module: assurance.checker.space.quadrant.northeast.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, cast

from domain.metadata.blueprint import NortheastQuadrantBlueprint
from err import NortheastQuadrantCarrierNullException, NortheastQuadrantRootCheckerException
from carrier import NortheastQuadrantCarrier
from domain.model import Vector
from artifcat import ValidationResult
from assurance.checker import QuadrantRootChecker
from space import NortheastQuadrant
from operation.toolkit.geometry.space.quadrant.northeast import NortheastQuadrantToolkit
from util import LoggingLevelRouter


class NortheastQuadrantRootChecker(QuadrantRootChecker[NortheastQuadrant]):
    """
    Role
        -   Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a NortheastQuadrantBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        bundle: NortheastQuadrantToolkit

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        IntegrityChecker
    """
    
    def __init__(self, bundle: NortheastQuadrantToolkit | None = NortheastQuadrantToolkit()):
        """
        Args:
            bundle: NortheastQuadrantToolkit
        """
        super().__init__(bundle=bundle)
    
    @property
    def toolkit(self) -> NortheastQuadrantBundle:
        return cast(NortheastQuadrantToolkit, super().ruleset)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[NortheastQuadrant | NortheastQuadrantBlueprint]:
        """
        Certify a candidate is a NortheastQuadrantBlueprint that is safe to use.

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
            NortheastQuadrantRootCheckerException
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
                NortheastQuadrantRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NortheastQuadrantRootCheckerException.MSG,
                    err_code=NortheastQuadrantRootCheckerException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(NortheastQuadrantCarrier, carrier_validation.payload)
        if carrier.is_not_carrying_anything:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NortheastQuadrantRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NortheastQuadrantRootCheckerException.MSG,
                    err_code=NortheastQuadrantRootCheckerException.ERR_CODE,
                    ex=NortheastQuadrantCarrierNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NortheastQuadrantCarrierNullException.MSG,
                        err_code=NortheastQuadrantCarrierNullException.ERR_CODE,
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
                    NortheastQuadrantRootCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NortheastQuadrantRootCheckerException.MSG,
                        err_code=NortheastQuadrantRootCheckerException.ERR_CODE,
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
                NortheastQuadrant(origin=origin)
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            NortheastQuadrantBlueprint(origin=origin)
        )