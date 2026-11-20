# src/exchange/service/validation/model/team/service.py

"""
Module: exchange.service.validation.model.team.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Team, TeamBlueprint
from err import TeamCarrierEmptyException, TeamValidationServiceException
from exchange import TeamValidationRequest
from microservice import ValidationMicroservice
from transit import TeamCarrier, TeamValidationDispatcher
from util import LoggingLevelRouter


class TeamValidationService(ValidationMicroservice[Team]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Team
                _   TeamBlueprint
            products from TeamValidationService.

    Attributes:
        dispatcher: TeamValidationDispatcher
        
    Provides:
        -   def extract_model(
                    request: TeamValidationRequest
            ) -> ValidationResult[Team]
            
        -   def extract_blueprint(
                    request: TeamValidationRequest
            ) -> ValidationResult[TeamBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[TeamValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[TeamValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or TeamValidationDispatcher())
    
    @property
    def dispatcher(self) -> TeamValidationDispatcher:
        return cast(TeamValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: TeamValidationRequest) -> ValidationResult[Team]:
        """
        Extract an Team safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Team from the result then send it to the client.
        Args:
            request: TeamValidationRequest
        Result:
            ValidationResult[Team]
        Raises:
            TeamValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationServiceException.MSG,
                    err_code=TeamValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(TeamCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationServiceException.MSG,
                    err_code=TeamValidationServiceException.ERR_CODE,
                    ex=TeamCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamCarrierEmptyException.MSG,
                        err_code=TeamCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Team, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: TeamValidationRequest,
    ) -> ValidationResult[TeamBlueprint]:
        """
        Extract an TeamBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the TeamBlueprint from the result then send it
                to the client.
        Args:
            request: TeamValidationRequest
        Result:
            ValidationResult[TeamBlueprint]
        Raises:
            TeamValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationServiceException.MSG,
                    err_code=TeamValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(TeamCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamValidationServiceException.MSG,
                    err_code=TeamValidationServiceException.ERR_CODE,
                    ex=TeamCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TeamCarrierEmptyException.MSG,
                        err_code=TeamCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(TeamBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)