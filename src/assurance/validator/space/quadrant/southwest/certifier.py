# src/assurance/validator/root/space/quadrant/southwest/assurance/checker.py

"""
Module: assurance.validator.space.quadrant.southwest.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, Optional, cast

from domain.metadata.blueprint import SouthwestQuadrantBlueprint
from carrier import SouthwestQuadrantCarrier
from domain.model import Vector
from artifcat import ValidationResult
from assurance.validator import QuadrantRootChecker
from space import SouthwestQuadrant
from operation.toolkit import SouthwestQuadrantToolkit

from util import LoggingLevelRouter


class SouthwestQuadrantRootChecker(QuadrantRootChecker[SouthwestQuadrantBlueprint]):
    """
    Role
        -  Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a SouthwestQuadrants or their blueprints are certified safe, reliable and consistent
            before use.

    Attributes:
        bundle: SouthwestQuadrantToolkit

    Provides:
        - def execute(self, candidate: Any) -> ValidationResult[SouthwestQuadrant|SouthwestQuadrantBlueprint]:

    Super Class:
        RootChecker
    """
    
    def __init__(self, bundle: Optional[SouthwestQuadrantToolkit]| None = None):
        """
        Args:
            bundle: SouthwestQuadrantToolkit
        """
        super().__init__(bundle=bundle or SouthwestQuadrantToolkit())
    
    @property
    def toolkit(self) -> SouthwestQuadrantBundle:
        return cast(SouthwestQuadrantToolkit, super().ruleset)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[SouthwestQuadrant|SouthwestQuadrantBlueprint]:
        """
        Certify a candidate is a SouthwestQuadrantBlueprint that is safe to use.

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
            SouthwestQuadrantRootCheckerException
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
                SouthwestQuadrantRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SouthwestQuadrantRootCheckerException.MSG,
                    err_code=SouthwestQuadrantRootCheckerException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(SouthwestQuadrantCarrier, carrier_validation.payload)
        if carrier.is_not_carrying_anything:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SouthwestQuadrantRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SouthwestQuadrantRootCheckerException.MSG,
                    err_code=SouthwestQuadrantRootCheckerException.ERR_CODE,
                    ex=SouthwestQuadrantCarrierNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SouthwestQuadrantCarrierNullException.MSG,
                        err_code=SouthwestQuadrantCarrierNullException.ERR_CODE,
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
                    SouthwestQuadrantRootCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SouthwestQuadrantRootCheckerException.MSG,
                        err_code=SouthwestQuadrantRootCheckerException.ERR_CODE,
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
                SouthwestQuadrant(origin=origin)
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            SouthwestQuadrantBlueprint(origin=origin)
        )