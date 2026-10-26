# src/bootstrap/validation/context/arena/loader.py

"""
Module: bootstrap.validation.context.arena.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, ArenaValidatorToolkit
from domain import Arena, ArenaContextPrimeExtract
from err import (
    ArenaCarrierEmptyException, ArenaContextValidationLoaderException, ArenaContextValidationRequestNullException
)
from exchange import ArenaContextValidationRequest
from transit import ArenaCarrier

from util import LoggingLevelRouter


class ArenaContextValidationLoader(ContextValidationLoader[ArenaContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ArenaContextValidationRequest
            -   ArenaCarrier
            -   ArenaBlueprint

    Attributes:
        toolkit: ArenaValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[ArenaContextPrimeExtract[T]

    Super Class:
        ContextValidationLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[ArenaValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[ArenaValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or ArenaValidatorToolkit())
    
    @property
    def toolkit(self) -> ArenaValidatorToolkit:
        return cast(ArenaValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ArenaContextPrimeExtract]:
        """
        Extract the ArenaBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a ArenaValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a ArenaCarrier
                        -   An empty ArenaCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a ArenaContextPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ArenaContextPrimeExtract]
        Raises:
            ArenaLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=ArenaContextValidationRequest,
            null_exception=ArenaContextValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaContextValidationLoaderException.MSG,
                    err_code=ArenaContextValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[ArenaContextValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaContextValidationLoaderException.MSG,
                    err_code=ArenaContextValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(ArenaContextCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaContextValidationLoaderException.MSG,
                    err_code=ArenaContextValidationLoaderException.ERR_CODE,
                    ex=ArenaCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ArenaCarrierEmptyException.MSG,
                        err_code=ArenaCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = ArenaContextPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)