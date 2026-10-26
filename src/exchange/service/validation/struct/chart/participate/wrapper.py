# src/exchange/service/validation/struct/chart/participate/service.py

"""
Module: exchange.service.validation.struct.chart.participate.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Participation, ParticipationBlueprint
from err import ParticipationValidationServiceException
from exchange import ChartValidationService, ParticipationValidationRequest, ParticipationValidationService
from util import LoggingLevelRouter


class ParticipationValidationService(
    ChartValidationService[Participation]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Token
                _   TokenBlueprint
            products from ParticipationValidationService.

    Attributes:
        service: ParticipationValidationService
        
    Provides:
        -   def extract_model(
                    request: ParticipationValidationRequest
            ) -> ValidationResult[Token]
            
        -   def extract_blueprint(
                    request: ParticipationValidationRequest
            ) -> ValidationResult[TokenBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[ParticipationValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[ParticipationValidationService]
        """
        super().__init__(service=service or ParticipationValidationService())
    
    @property
    def service(self) -> ParticipationValidationService:
        return cast(ParticipationValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: ParticipationValidationRequest,
    ) -> ValidationResult[Participation]:
        """
        Extract a Token safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Token from the success response then send it 
                to the client.
        Args:
            request: ParticipationValidationRequest
        Result:
            ValidationResult[Token]
        Raises:
            ParticipationValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidationServiceException.MSG,
                    err_code=ParticipationValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ParticipationValidationResponse, result)
        if not response.valid_chart:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidationServiceException.MSG,
                    err_code=ParticipationValidationServiceException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        chart = cast(Participation, response.valid_chart)
        return ValidationResult.success(chart)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: ParticipationValidationRequest,
    ) -> ValidationResult[ParticipationBlueprint]:
        """
        Extract a TokenBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the TokenBluprint from the success response
                then send it to the client.
        Args:
            request: ParticipationValidationRequest
        Result:
            ValidationResult[TokenBlueprint]
        Raises:
            ParticipationValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidationServiceException.MSG,
                    err_code=ParticipationValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ParticipationValidationResponse, result)
        if not response.valid_token:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidationServiceException.MSG,
                    err_code=ParticipationValidationServiceException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(ParticipationBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)