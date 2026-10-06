# src/assurance/load/model/team/loader.py

"""
Module: assurance.load.model.team.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelLoader, TeamValidatorToolkit
from domain import Team, TeamPrimeExtract
from err import (
    TeamCarrierEmptyException, TeamLoaderException, TeamValidationRequestNullException
)
from exchange import TeamValidationRequest
from transit import TeamCarrier

from util import LoggingLevelRouter


class TeamLoader(ModelLoader[Team]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   TeamValidationRequest
            -   TeamCarrier
            -   TeamBlueprint

    Attributes:
        toolkit: TeamValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[TeamPrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[TeamValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TeamValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or TeamValidatorToolkit())
    
    @property
    def toolkit(self) -> TeamValidatorToolkit:
        return cast(TeamValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TeamPrimeExtract]:
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
            candidate: Any
        Returns:
            ValidationResult[TeamPrimeExtract]
        Raises:
            TeamLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=TeamValidationRequest,
            null_exception=TeamValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamLoaderException.MSG,
                    err_code=TeamLoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result to request for additional tests. ---#
        request = cast(Type[TeamValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamLoaderException.MSG,
                    err_code=TeamLoaderException.ERR_CODE,
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
                TeamLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamLoaderException.MSG,
                    err_code=TeamLoaderException.ERR_CODE,
                    ex=TeamCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamCarrierEmptyException.MSG,
                        err_code=TeamCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = TeamPrimeExtract(reference=carrier, safe_blueprint=blueprint)
        return ValidationResult.success(extract)