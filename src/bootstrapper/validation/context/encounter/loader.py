# src/bootstrap/validation/context/encounter/loader.py

"""
Module: bootstrap.validation.context.encounter.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, EncounterValidatorToolkit
from domain import Encounter, Encounter
from err import (
    EncounterCarrierEmptyException, EncounterContextValidationLoaderException,
    EncounterValidationRequestNullException
)
from exchange import EncounterValidationRequest
from transit import EncounterCarrier

from util import LoggingLevelRouter


class EncounterContextValidationLoader(ContextValidationLoader[Encounter]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   EncounterValidationRequest
            -   EncounterCarrier
            -   EncounterBlueprint

    Attributes:
        toolkit: EncounterValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[Encounter[T]

    Super Class:
        ContextLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[EncounterValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[EncounterValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or EncounterValidatorToolkit())
    
    @property
    def toolkit(self) -> EncounterValidatorToolkit:
        return cast(EncounterValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[Encounter]:
        """
        Extract the EncounterBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a EncounterValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a EncounterCarrier
                        -   An empty EncounterCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a Encounter
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Encounter]
        Raises:
            EncounterLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_context=EncounterValidationRequest,
            null_exception=EncounterValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterContextValidationLoaderException.MSG,
                    err_code=EncounterContextValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[EncounterValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_context=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterContextValidationLoaderException.MSG,
                    err_code=EncounterContextValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(EncounterCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterContextValidationLoaderException.MSG,
                    err_code=EncounterContextValidationLoaderException.ERR_CODE,
                    ex=EncounterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterCarrierEmptyException.MSG,
                        err_code=EncounterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = Encounter(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)