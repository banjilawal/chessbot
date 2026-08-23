# src/assurance/checker/root/space/axis/north/assurance/checker.py

"""
Module: assurance.checker.space.axis.north.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, List, cast

from domain.metadata.blueprint import NorthAxisBlueprint
from carrier import NorthAxisCarrier
from err import NorthAxisCarrierNullException, NorthAxisRootCheckerException
from domain.model import Vector
from artifcat.result import ValidationResult
from assurance.checker import AxisRootChecker
from space import NorthAxis
from operation.toolkit.geometry.space.axis.north import NorthAxisToolkit
from util import LoggingLevelRouter


class NorthAxisRootChecker(AxisRootChecker[NorthAxisBlueprint]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a NorthAxisBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        bundle: NorthAxisToolkit

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        IntegrityChecker
    """
    
    def __init__(self, bundle: NorthAxisToolkit | None = NorthAxisToolkit()):
        """
        Args:
            bundle: NorthAxisToolkit
        """
        super().__init__(bundle=bundle)
    
    @property
    def toolkit(self) -> NorthAxisBundle:
        return cast(NorthAxisToolkit, super().ruleset)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[NorthAxis| NorthAxisBlueprint]:
        """
        Certify a candidate is a NorthAxisBlueprint that is safe to use.

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
            NorthAxisRootCheckerException
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
                NorthAxisRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NorthAxisRootCheckerException.MSG,
                    err_code=NorthAxisRootCheckerException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        carrier = cast(NorthAxisCarrier, carrier_validation.payload)
        if carrier.is_not_carrying_anything:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NorthAxisRootCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NorthAxisRootCheckerException.MSG,
                    err_code=NorthAxisRootCheckerException.ERR_CODE,
                    ex=NorthAxisCarrierNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NorthAxisCarrierNullException.MSG,
                        err_code=NorthAxisCarrierNullException.ERR_CODE,
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
                    NorthAxisRootCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NorthAxisRootCheckerException.MSG,
                        err_code=NorthAxisRootCheckerException.ERR_CODE,
                        ex=vector_validation.exception,
                    )
                )
            vectors.append(cast(Vector, vector_validation.payload))
        # --- Extract and cast payloads of the validation results. ---#
        origin = vectors[0]

        if carrier.is_carrying_model:
            return ValidationResult.success(
                NorthAxis(origin=origin)
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            NorthAxisBlueprint(origin=origin)
        )