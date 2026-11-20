# src/exchange/service/validation/model/rank/service.py

"""
Module: exchange.service.validation.model.rank.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Rank, RankBlueprint
from err import RankCarrierEmptyException, RankValidationServiceException
from exchange import RankValidationRequest
from microservice import ValidationMicroservice
from transit import RankCarrier, RankValidationDispatcher
from util import LoggingLevelRouter


class RankValidationService(ValidationMicroservice[Rank]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Rank
                _   RankBlueprint
            products from RankValidationService.

    Attributes:
        dispatcher: RankValidationDispatcher
        
    Provides:
        -   def extract_model(
                    request: RankValidationRequest
            ) -> ValidationResult[Rank]
            
        -   def extract_blueprint(
                    request: RankValidationRequest
            ) -> ValidationResult[RankBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[RankValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[RankValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or RankValidationDispatcher())
    
    @property
    def dispatcher(self) -> RankValidationDispatcher:
        return cast(RankValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: RankValidationRequest) -> ValidationResult[Rank]:
        """
        Extract an Rank safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Rank from the result then send it to the client.
        Args:
            request: RankValidationRequest
        Result:
            ValidationResult[Rank]
        Raises:
            RankValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationServiceException.MSG,
                    err_code=RankValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(RankCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationServiceException.MSG,
                    err_code=RankValidationServiceException.ERR_CODE,
                    ex=RankCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RankCarrierEmptyException.MSG,
                        err_code=RankCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Rank, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: RankValidationRequest,
    ) -> ValidationResult[RankBlueprint]:
        """
        Extract an RankBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the RankBlueprint from the result then send it
                to the client.
        Args:
            request: RankValidationRequest
        Result:
            ValidationResult[RankBlueprint]
        Raises:
            RankValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationServiceException.MSG,
                    err_code=RankValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(RankCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationServiceException.MSG,
                    err_code=RankValidationServiceException.ERR_CODE,
                    ex=RankCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RankCarrierEmptyException.MSG,
                        err_code=RankCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(RankBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)