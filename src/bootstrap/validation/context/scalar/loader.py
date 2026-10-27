# src/bootstrap/validation/context/scalar/loader.py

"""
Module: bootstrap.validation.context.scalar.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, ScalarLayerToolkit
from domain import Scalar, ScalarContextPrimeExtract
from err import (
    ScalarCarrierEmptyException, ScalarContextValidationLoaderException, ScalarContextValidationRequestNullException
)
from exchange import ScalarContextValidationRequest
from transit import ScalarCarrier

from util import LoggingLevelRouter


class ScalarContextValidationLoader(ContextValidationLoader[ScalarContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ScalarContextValidationRequest
            -   ScalarCarrier
            -   ScalarBlueprint

    Attributes:
        toolkit: ScalarLayerToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[ScalarContextPrimeExtract[T]

    Super Class:
        ContextValidationLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[ScalarLayerToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[ScalarLayerToolkit]
        """
        super().__init__(toolkit=toolkit or ScalarLayerToolkit())
    
    @property
    def toolkit(self) -> ScalarLayerToolkit:
        return cast(ScalarLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ScalarContextPrimeExtract]:
        """
        Extract the ScalarBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a ScalarValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a ScalarCarrier
                        -   An empty ScalarCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a ScalarContextPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ScalarContextPrimeExtract]
        Raises:
            ScalarLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the wrong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=ScalarContextValidationRequest,
            null_exception=ScalarContextValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarContextValidationLoaderException.MSG,
                    err_code=ScalarContextValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[ScalarContextValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarContextValidationLoaderException.MSG,
                    err_code=ScalarContextValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(ScalarContextCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarContextValidationLoaderException.MSG,
                    err_code=ScalarContextValidationLoaderException.ERR_CODE,
                    ex=ScalarCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ScalarCarrierEmptyException.MSG,
                        err_code=ScalarCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = ScalarContextPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)