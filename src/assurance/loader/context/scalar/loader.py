# src/assurance/load/context/scalar/loader.py

"""
Module: assurance.load.context.scalar.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, ScalarValidatorToolkit
from domain import Scalar, Scalar
from err import (
    ScalarCarrierEmptyException, ScalarContextValidationLoaderException, ScalarValidationRequestNullException
)
from exchange import ScalarValidationRequest
from transit import ScalarCarrier

from util import LoggingLevelRouter


class ScalarContextValidationLoader(ContextValidationLoader[Scalar]):
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
            ) -> ValidationResult[Scalar[T]

    Super Class:
        ContextLoader
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
    def execute(self, candidate: Any) -> ValidationResult[Scalar]:
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
            2.  Otherwise, pack the original carrier and the blueprint in a Scalar
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Scalar]
        Raises:
            ScalarLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the wrong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_context=ScalarValidationRequest,
            null_exception=ScalarValidationRequestNullException(),
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
        request = cast(Type[ScalarValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_context=self.toolkit.types.carrier,
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
        carrier = cast(ScalarCarrier, carrier_validation.payload)
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
        extract = Scalar(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)