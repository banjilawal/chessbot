# src/bootstrap/validation/model/team/loader.py

"""
Module: bootstrap.validation.context.team.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import TeamLayerToolkit
from bootstrap import ModelValidationLoader
from domain import Team, TeamPrimeExtract
from err import (
    TeamCarrierEmptyException, TeamValidationLoaderException, TeamValidationRequestNullException
)
from exchange import TeamValidationRequest
from transit import TeamCarrier

from util import LoggingLevelRouter


class TeamValidationLoader(ModelValidationLoader[Team]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   TeamValidationRequest
            -   TeamCarrier
            -   TeamBlueprint

    Attributes:
        toolkit: TeamLayerToolkit

    Provides:
        -   def execute(item: Any) -> ValidationResult[TeamPrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[TeamLayerToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TeamLayerToolkit]
        """
        super().__init__(toolkit=toolkit or TeamLayerToolkit())
    
    @property
    def toolkit(self) -> TeamLayerToolkit:
        return cast(TeamLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[TeamPrimeExtract]:
        """
        Extract the TeamBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a TeamValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a TeamCarrier
                        -   An empty TeamCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a TeamPrimeExtract
                for the success result.
        Args:
            item: Any
        Returns:
            ValidationResult[TeamPrimeExtract]
        Raises:
            TeamLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=item,
            target_model=TeamValidationRequest,
            null_exception=TeamValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationLoaderException.MSG,
                    err_code=TeamValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[TeamValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationLoaderException.MSG,
                    err_code=TeamValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(TeamCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationLoaderException.MSG,
                    err_code=TeamValidationLoaderException.ERR_CODE,
                    ex=TeamCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamCarrierEmptyException.MSG,
                        err_code=TeamCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = TeamPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)