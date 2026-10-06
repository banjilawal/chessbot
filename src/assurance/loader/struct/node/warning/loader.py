# src/assurance/load/struct/node/warning/loader.py

"""
Module: assurance.load.struct.node.warning.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import NodeLoader, EncounterWarningNodeValidatorToolkit
from domain import EncounterWarningNode, EncounterWarningNodePrimeExtract
from err import (
    EncounterWarningNodeCarrierEmptyException, EncounterWarningNodeLoaderException,
    EncounterWarningNodeValidationRequestNullException
)
from exchange import EncounterWarningNodeValidationRequest
from transit import EncounterWarningNodeCarrier

from util import LoggingLevelRouter


class EncounterWarningNodeLoader(NodeLoader[EncounterWarningNode]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   EncounterWarningNodeValidationRequest
            -   EncounterWarningNodeCarrier
            -   EncounterWarningNodeBlueprint

    Attributes:
        toolkit: EncounterWarningNodeValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[EncounterWarningNodePrimeExtract[T]

    Super Class:
        NodeLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[EncounterWarningNodeValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[EncounterWarningNodeValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or EncounterWarningNodeValidatorToolkit())
    
    @property
    def toolkit(self) -> EncounterWarningNodeValidatorToolkit:
        return cast(EncounterWarningNodeValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[EncounterWarningNodePrimeExtract]:
        """
        Extract the EncounterWarningNodeBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a EncounterWarningNodeValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a EncounterWarningNodeCarrier
                        -   An empty EncounterWarningNodeCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a EncounterWarningNodePrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[EncounterWarningNodePrimeExtract]
        Raises:
            EncounterWarningNodeLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=EncounterWarningNodeValidationRequest,
            null_exception=EncounterWarningNodeValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterWarningNodeLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWarningNodeLoaderException.MSG,
                    err_code=EncounterWarningNodeLoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result to request for additional tests. ---#
        request = cast(Type[EncounterWarningNodeValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterWarningNodeLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWarningNodeLoaderException.MSG,
                    err_code=EncounterWarningNodeLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(EncounterWarningNodeCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterWarningNodeLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWarningNodeLoaderException.MSG,
                    err_code=EncounterWarningNodeLoaderException.ERR_CODE,
                    ex=EncounterWarningNodeCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterWarningNodeCarrierEmptyException.MSG,
                        err_code=EncounterWarningNodeCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = EncounterWarningNodePrimeExtract(reference=carrier, safe_blueprint=blueprint)
        return ValidationResult.success(extract)