# src/bootstrap/validation/struct/node/warning/loader.py

"""
Module: bootstrap.validation.struct.node.warning.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import NodeValidationLoader, EncounterWarningNodeValidatorToolkit
from domain import EncounterWarningNode, EncounterWarningNode
from err import (
    EncounterWarningNodeCarrierEmptyException, EncounterWarningNodeLoaderException,
    EncounterWarningNodeValidationRequestNullException
)
from exchange import EncounterWarningNodeValidationRequest
from transit import EncounterWarningNodeCarrier

from util import LoggingLevelRouter


class EncounterWarningNodeLoader(NodeValidationLoader[EncounterWarningNode]):
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
            ) -> ValidationResult[EncounterWarningNode[T]

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
    def execute(self, candidate: Any) -> ValidationResult[EncounterWarningNode]:
        """
        Model the EncounterWarningNodeBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a EncounterWarningNodeValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a EncounterWarningNodeCarrier
                        -   An empty EncounterWarningNodeCarrier.
                -   A blueprint cannot be modeled from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a EncounterWarningNode
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[EncounterWarningNode]
        Raises:
            EncounterWarningNodeLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=EncounterWarningNodeValidationRequest,
            null_exception=EncounterWarningNodeValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterWarningNodeLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWarningNodeLoaderException.MSG,
                    err_code=EncounterWarningNodeLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[EncounterWarningNodeValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        model_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.model,
            null_exception=self.toolkit.nulls.model,
        )
        if model_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterWarningNodeLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWarningNodeLoaderException.MSG,
                    err_code=EncounterWarningNodeLoaderException.ERR_CODE,
                    ex=model_validation.exception,
                )
            )
        # --- Cast model_validation payload to carrier then model blueprint. ---#
        carrier = cast(EncounterWarningNodeCarrier, model_validation.payload)
        blueprint = carrier.model_blueprint()
        
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
        model = EncounterWarningNode(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(model)