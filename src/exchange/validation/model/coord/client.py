# src/exchange/validation/model/coord/exchange.py

"""
Module: exchange.validation.model.coord.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, CoordValidationResponse
from exchange import ModelValidationResponseService, CoordValidationRequest
from domain import Coord
from err import CoordValidatorResponseServiceException
from transit import CoordCarrier, CoordValidationDispatcher
from util import LoggingLevelRouter


class CoordValidationResponseService(ModelValidationResponseService[Coord]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Coord validation Request-Response workflow.

    Attributes:
        dispatcher: CoordValidationDispatcher[T]

    Provides:
        -   def submit(request: CoordValidationRequest[T]) -> CoordValidationResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[CoordValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[CoordValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or CoordValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> CoordValidationDispatcher:
        return cast(CoordValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: CoordValidationRequest
    ) -> CoordValidationResponse:
        """
        Certify a candidate is a CoordCarrier whose payload is either a Coord
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: CoordValidationRequest
        Result:
            CoordValidationResponse
        Raises:
            CoordValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return CoordValidationResponse.failure(
                request=request,
                result=result,
                exception=CoordValidatorResponseServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidatorResponseServiceException.MSG,
                    err_code=CoordValidatorResponseServiceException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(CoordCarrier, result.payload)
        return CoordValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )