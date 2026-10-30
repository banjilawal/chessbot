# src/exchange/service/validation/context/team/service.py

"""
Module: exchange.service.validation.context.team.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import TeamValidationResponse, ValidationResult
from domain import Team, TeamBlueprint
from err import TeamContextValidationServiceException, TeamContextValidationServiceException, TeamCarrierEmptyException
from exchange import (
    TeamContextValidationService, ContextValidationService, TeamValidationRequest
)
from util import LoggingLevelRouter


class TeamContextValidationService(
    ContextValidationService[Team]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Team
                _   TeamBlueprint
            products from TeamContextValidationService.

    Attributes:
        service: TeamContextValidationService
        
    Provides:
        -   def extract_context(
                    request: TeamValidationRequest
            ) -> ValidationResult[Team]
            
        -   def extract_blueprint(
                    request: TeamValidationRequest
            ) -> ValidationResult[TeamBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[TeamContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[TeamContextValidationService]
        """
        super().__init__(service=service or TeamContextValidationService())
    
    @property
    def service(self) -> TeamContextValidationService:
        return cast(TeamContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
            self, 
            request: TeamValidationRequest,
    ) -> ValidationResult[Team]:
        """
        Extract a Team safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Team from the success response then send it 
                to the client.
        Args:
            request: TeamValidationRequest
        Result:
            ValidationResult[Team]
        Raises:
            TeamContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamContextValidationServiceException.MSG,
                    err_code=TeamContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TeamValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamContextValidationServiceException.MSG,
                    err_code=TeamContextValidationServiceException.ERR_CODE,
                    ex=TeamCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamCarrierEmptyException.MSG,
                        err_code=TeamCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Team, response.valid_context)
        return ValidationResult.success(context)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: TeamValidationRequest,
    ) -> ValidationResult[TeamBlueprint]:
        """
        Extract a TeamBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the TeamBluprint from the success response
                then send it to the client.
        Args:
            request: TeamValidationRequest
        Result:
            ValidationResult[TeamBlueprint]
        Raises:
            TeamContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamContextValidationServiceException.MSG,
                    err_code=TeamContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TeamValidationResponse, result)
        if not response.valid_team:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamContextValidationServiceException.MSG,
                    err_code=TeamContextValidationServiceException.ERR_CODE,
                    ex=TeamCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamCarrierEmptyException.MSG,
                        err_code=TeamCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(TeamBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)