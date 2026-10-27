# src/bootstrap/validation/struct/chart/participate/loader.py

"""
Module: bootstrap.validation.struct.chart.participate.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ChartValidationLoader, ParticipationLayerToolkit
from domain import Participation, Participation
from err import (
    ParticipationCarrierEmptyException, ParticipationLoaderException,
    ParticipationValidationRequestNullException
)
from exchange import FootstepValidationRequest
from transit import ParticipationCarrier

from util import LoggingLevelRouter


class ParticipationLoader(ChartValidationLoader[Participation]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ParticipationValidationRequest
            -   ParticipationCarrier
            -   ParticipationBlueprint

    Attributes:
        toolkit: ParticipationLayerToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[Participation[T]

    Super Class:
        ChartLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[ParticipationLayerToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[ParticipationLayerToolkit]
        """
        super().__init__(toolkit=toolkit or ParticipationLayerToolkit())
    
    @property
    def toolkit(self) -> ParticipationLayerToolkit:
        return cast(ParticipationLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[Participation]:
        """
        Model the ParticipationBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a ParticipationValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a ParticipationCarrier
                        -   An empty ParticipationCarrier.
                -   A blueprint cannot be modeled from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a Participation
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Participation]
        Raises:
            ParticipationLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=FootstepValidationRequest,
            null_exception=ParticipationValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationLoaderException.MSG,
                    err_code=ParticipationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[FootstepValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        model_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.model,
            null_exception=self.toolkit.nulls.model,
        )
        if model_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationLoaderException.MSG,
                    err_code=ParticipationLoaderException.ERR_CODE,
                    ex=model_validation.exception,
                )
            )
        # --- Cast model_validation payload to carrier then model blueprint. ---#
        carrier = cast(ParticipationCarrier, model_validation.payload)
        blueprint = carrier.model_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationLoaderException.MSG,
                    err_code=ParticipationLoaderException.ERR_CODE,
                    ex=ParticipationCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ParticipationCarrierEmptyException.MSG,
                        err_code=ParticipationCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = Participation(
            reference=carrier,
            blueprint=blueprint,
        )
        return ValidationResult.success(model)