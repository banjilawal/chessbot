# src/exchange/responder/fabrication/model/rank/responder.py

"""
Module: exchange.responder.fabrication.model.rank.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, RankBuildResponse
from exchange import ModelBuildResponder, RankBuildRequest
from domain import Rank
from err import RankBuildResponderException
from transit import RankCarrier, RankBuildDispatcher
from util import LoggingLevelRouter


class RankBuildResponder(ModelBuildResponder[Rank]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Rank build Request-Response workflow.

    Attributes:
        dispatcher: RankBuildDispatcher[T]

    Provides:
        -   def submit(request: RankBuildRequest[T]) -> RankBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[RankBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[RankBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or RankBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> RankBuildDispatcher:
        return cast(RankBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: RankBuildRequest
    ) -> RankBuildResponse:
        """
        Certify a candidate is a RankCarrier whose payload is either a Rank
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: RankBuildRequest
        Result:
            RankBuildResponse
        Raises:
            RankValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return RankBuildResponse.failure(
                request=request,
                result=result,
                exception=RankBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankBuildResponderException.MSG,
                    err_code=RankBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(RankCarrier, result.payload)
        return RankBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )