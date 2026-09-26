# src/client/validation/model/rank/client.py

"""
Module: client.validation.model.rank.client
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, RankValidationResponse
from client import ModelValidatorClient, RankValidationRequest
from domain import Rank
from err import RankValidatorClientException
from transit import RankCarrier, RankValidationDispatcher
from util import LoggingLevelRouter


class RankValidatorClient(ModelValidatorClient[Rank]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Rank validation Request-Response workflow.

    Attributes:
        dispatcher: RankValidationDispatcher[T]

    Provides:
        -   def submit(request: RankValidationRequest[T]) -> RankValidationResponse[T]

    Super Class:
        ModelValidatorClient
    """
    
    def __init__(
            self, 
            dispatcher: Optional[RankValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[RankValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or RankValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> RankValidationDispatcher:
        return cast(RankValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def transmit(
            self,
            request: RankValidationRequest
    ) -> RankValidationResponse:
        """
        Certify a candidate is a RankCarrier whose payload is either a Rank
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: RankValidationRequest
        Result:
            RankValidationResponse
        Raises:
            RankValidatorClientException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return RankValidationResponse.failure(
                request=request,
                result=result,
                exception=RankValidatorClientException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidatorClientException.MSG,
                    err_code=RankValidatorClientException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(RankCarrier, result.payload)
        return RankValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )