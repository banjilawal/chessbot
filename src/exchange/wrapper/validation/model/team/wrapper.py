# src/exchange/wrapper/validation/model/team/wrapper.py

"""
Module: exchange.wrapper.validation.model.team.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import TeamValidationResponse, ValidationResult
from domain import Team, TeamBlueprint
from err import TeamValidationResponderException, TeamValidationResponseWrapperException, EmptyTeamCarrierException
from exchange import (
    TeamValidationResponder, ModelValidationResponseWrapper, TeamValidationRequest
)
from util import LoggingLevelRouter


class TeamValidationResponseWrapper(
    ModelValidationResponseWrapper[Team]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Team
                _   TeamBlueprint
            products from TeamValidationResponder.

    Attributes:
        responder: TeamValidationResponder
        
    Provides:
        -   def extract_model(
                    request: TeamValidationRequest
            ) -> ValidationResult[Team]
            
        -   def extract_blueprint(
                    request: TeamValidationRequest
            ) -> ValidationResult[TeamBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[TeamValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[TeamValidationResponder]
        """
        super().__init__(responder=responder or TeamValidationResponder())
    
    @property
    def responder(self) -> TeamValidationResponder:
        return cast(TeamValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: TeamValidationRequest,
    ) -> ValidationResult[Team]:
        """
        Extract a Team safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Team from the success response then send it 
                to the client.
        Args:
            request: TeamValidationRequest
        Result:
            ValidationResult[Team]
        Raises:
            TeamValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationResponseWrapperException.MSG,
                    err_code=TeamValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TeamValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationResponderException.MSG,
                    err_code=TeamValidationResponderException.ERR_CODE,
                    ex=EmptyTeamCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyTeamCarrierException.MSG,
                        err_code=EmptyTeamCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Team, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: TeamValidationRequest,
    ) -> ValidationResult[TeamBlueprint]:
        """
        Extract a TeamBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the TeamBluprint from the success response
                then send it to the client.
        Args:
            request: TeamValidationRequest
        Result:
            ValidationResult[TeamBlueprint]
        Raises:
            TeamValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationResponseWrapperException.MSG,
                    err_code=TeamValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TeamValidationResponse, result)
        if not response.valid_team:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationResponderException.MSG,
                    err_code=TeamValidationResponderException.ERR_CODE,
                    ex=EmptyTeamCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyTeamCarrierException.MSG,
                        err_code=EmptyTeamCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(TeamBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)