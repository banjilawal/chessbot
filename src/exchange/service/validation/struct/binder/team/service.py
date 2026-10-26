# src/exchange/service/validation/struct/binder/team/service.py

"""
Module: exchange.service.validation.struct.binder.team.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import TeamBinderValidationResponse, ValidationResult
from domain import  TeamBinder, TeamBinderBlueprint
from err import TeamBinderValidationServiceException, TeamBinderValidationServiceException, TeamCarrierEmptyException

from util import LoggingLevelRouter


class TeamBinderValidationService(
    BinderValidationService[TeamBinder]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Team
                _   TeamBlueprint
            products from TeamBinderValidationService.

    Attributes:
        service: TeamBinderValidationService
        
    Provides:
        -   def extract_model(
                    request: TeamBinderValidationRequest
            ) -> ValidationResult[Team]
            
        -   def extract_blueprint(
                    request: TeamBinderValidationRequest
            ) -> ValidationResult[TeamBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[TeamBinderValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[TeamBinderValidationService]
        """
        super().__init__(service=service or TeamBinderValidationService())
    
    @property
    def service(self) -> TeamBinderValidationService:
        return cast(TeamBinderValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: TeamBinderValidationRequest,
    ) -> ValidationResult[TeamBinder]:
        """
        Extract a Team safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Team from the success response then send it 
                to the client.
        Args:
            request: TeamBinderValidationRequest
        Result:
            ValidationResult[Team]
        Raises:
            TeamBinderValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidationServiceException.MSG,
                    err_code=TeamBinderValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TeamBinderValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidationServiceException.MSG,
                    err_code=TeamBinderValidationServiceException.ERR_CODE,
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
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the TeamBluprint from the success response
                then send it to the client.
        Args:
            request: TeamBinderValidationRequest
        Result:
            ValidationResult[TeamBlueprint]
        Raises:
            TeamBinderValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidationServiceException.MSG,
                    err_code=TeamBinderValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(TeamBinderValidationResponse, result)
        if not response.valid_team:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderValidationServiceException.MSG,
                    err_code=TeamBinderValidationServiceException.ERR_CODE,
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