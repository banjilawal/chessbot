# src/exchange/server/validation/struct/binder/team/server.py

"""
Module: exchange.server.validation.struct.binder.team.server
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import TeamBinderValidationResponse, ValidationResult
from domain import Team, TeamBlueprint, TeamBinder, TeamBinderBlueprint
from err import TeamBinderValidationResponderException, TeamBinderValidationServerException, TeamCarrierEmptyException
from exchange import (
    TeamBinderValidationResponder, BinderValidationService, TeamBinderValidationRequest
)
from util import LoggingLevelRouter


class TeamBinderValidationServer(
    BinderValidationService[TeamBinder]
):
    """
    Role
        -   Server

    Responsibilities:
        1.  Extract either safe:
                -   Team
                _   TeamBlueprint
            products from TeamBinderValidationResponder.

    Attributes:
        responder: TeamBinderValidationResponder
        
    Provides:
        -   def extract_model(
                    request: TeamBinderValidationRequest
            ) -> ValidationResult[Team]
            
        -   def extract_blueprint(
                    request: TeamBinderValidationRequest
            ) -> ValidationResult[TeamBlueprint]

    Super Class:
        ValidationServer
    """
    
    def __init__(
            self,
            responder: Optional[TeamBinderValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[TeamBinderValidationResponder]
        """
        super().__init__(responder=responder or TeamBinderValidationResponder())
    
    @property
    def responder(self) -> TeamBinderValidationResponder:
        return cast(TeamBinderValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: TeamBinderValidationRequest,
    ) -> ValidationResult[TeamBinder]:
        """
        Extract a Team safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Team from the success response then send it 
                to the client.
        Args:
            request: TeamBinderValidationRequest
        Result:
            ValidationResult[Team]
        Raises:
            TeamBinderValidationServerException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationServerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidationServerException.MSG,
                    err_code=TeamBinderValidationServerException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TeamBinderValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidationResponderException.MSG,
                    err_code=TeamBinderValidationResponderException.ERR_CODE,
                    ex=TeamCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamCarrierEmptyException.MSG,
                        err_code=TeamCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        binder = cast(TeamBinder, response.valid_model)
        return ValidationResult.success(binder)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: TeamBinderValidationRequest,
    ) -> ValidationResult[TeamBinderBlueprint]:
        """
        Extract a TeamBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the TeamBluprint from the success response
                then send it to the client.
        Args:
            request: TeamBinderValidationRequest
        Result:
            ValidationResult[TeamBlueprint]
        Raises:
            TeamBinderValidationServerException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationServerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidationServerException.MSG,
                    err_code=TeamBinderValidationServerException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TeamBinderValidationResponse, result)
        if not response.valid_team:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidationResponderException.MSG,
                    err_code=TeamBinderValidationResponderException.ERR_CODE,
                    ex=TeamCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamCarrierEmptyException.MSG,
                        err_code=TeamCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(TeamBinderBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)