# src/assurance/load/model/scalar/loader.py

"""
Module: assurance.load.model.scalar.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelLoader, ScalarValidatorToolkit
from domain import Scalar, ScalarPrimeExtract
from err import (
    EmptyScalarCarrierException, ScalarLoaderException, ScalarValidationRequestNullException
)
from exchange import ScalarValidationRequest
from transit import ScalarCarrier

from util import LoggingLevelRouter


class ScalarLoader(ModelLoader[Scalar]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ScalarValidationRequest
            -   ScalarCarrier
            -   ScalarBlueprint

    Attributes:
        toolkit: ScalarValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[ScalarPrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[ScalarValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[ScalarValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or ScalarValidatorToolkit())
    
    @property
    def toolkit(self) -> ScalarValidatorToolkit:
        return cast(ScalarValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ScalarPrimeExtract]:
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
            2.  Otherwise, pack the original carrier and the blueprint in a ScalarPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ScalarPrimeExtract]
        Raises:
            ScalarLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=ScalarValidationRequest,
            null_exception=ScalarValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarLoaderException.MSG,
                    err_code=ScalarLoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result to request for additional tests. ---#
        request = cast(Type[ScalarValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarLoaderException.MSG,
                    err_code=ScalarLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(ScalarCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarLoaderException.MSG,
                    err_code=ScalarLoaderException.ERR_CODE,
                    ex=EmptyScalarCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyScalarCarrierException.MSG,
                        err_code=EmptyScalarCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = ScalarPrimeExtract(carrier=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)