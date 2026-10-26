# src/bootstrap/validation/context/alert/loader.py

"""
Module: bootstrap.validation.context.alert.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, AlertValidatorToolkit
from domain import Alert, AlertContextPrimeExtract
from err import (
    AlertCarrierEmptyException, AlertContextValidationLoaderException, AlertContextValidationRequestNullException
)
from exchange import AlertContextValidationRequest
from transit import AlertCarrier

from util import LoggingLevelRouter


class AlertContextValidationLoader(ContextValidationLoader[AlertContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   AlertContextValidationRequest
            -   AlertCarrier
            -   AlertBlueprint

    Attributes:
        toolkit: AlertValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[AlertContextPrimeExtract[T]

    Super Class:
        ContextValidationLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[AlertValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[AlertValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or AlertValidatorToolkit())
    
    @property
    def toolkit(self) -> AlertValidatorToolkit:
        return cast(AlertValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[AlertContextPrimeExtract]:
        """
        Extract the AlertBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a AlertValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not an AlertCarrier
                        -   An empty AlertCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a AlertContextPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[AlertContextPrimeExtract]
        Raises:
            AlertLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=AlertContextValidationRequest,
            null_exception=AlertContextValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertContextValidationLoaderException.MSG,
                    err_code=AlertContextValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[AlertContextValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertContextValidationLoaderException.MSG,
                    err_code=AlertContextValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(AlertContextCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertContextValidationLoaderException.MSG,
                    err_code=AlertContextValidationLoaderException.ERR_CODE,
                    ex=AlertCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AlertCarrierEmptyException.MSG,
                        err_code=AlertCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = AlertContextPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)