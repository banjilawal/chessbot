# src/assurance/loader/loader.py

"""
Module: assurance.loader.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelBlueprintLoader, TeamValidatorToolkit
from client import TeamValidationRequest
from domain import Team, TeamBlueprint
from err import EmptyTeamCarrierException, TeamValidationRequestNullException, TeamBlueprintLoaderException
from transit import TeamCarrier
from util import LoggingLevelRouter


class TeamBlueprintLoader(ModelBlueprintLoader[Team]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Extract a TeamBlueprint from the validation candidate.

    Attributes:
        toolkit: TeamValidatorToolkit

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[TeamBlueprint]:

    Super Class:
        ModelBlueprintLoader
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
    def execute(self, candidate: Any) -> ValidationResult[TeamBlueprint]:
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
            2.  Otherwise, send the blueprint in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TeamBlueprint]
        Raises:
            TeamBlueprintLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.helper.priming_validator.execute(
            candidate=candidate,
            target_model=TeamValidationRequest,
            null_exception=TeamValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBlueprintLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBlueprintLoaderException.MSG,
                    err_code=TeamBlueprintLoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result into a request for additional tests. ---#
        request = cast(Type[TeamValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBlueprintLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBlueprintLoaderException.MSG,
                    err_code=TeamBlueprintLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to into carrier to extract the blueprint. ---#
        carrier = cast(TeamCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBlueprintLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBlueprintLoaderException.MSG,
                    err_code=TeamBlueprintLoaderException.ERR_CODE,
                    ex=EmptyTeamCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyTeamCarrierException.MSG,
                        err_code=EmptyTeamCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(blueprint)