# src/exchange/responder/authorization/model/rank/responder.py

"""
Module: exchange.responder.authorization.model.rank.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, RankDecision
from exchange import ModelAuthorizationResponder, RankAuthorizationRequest
from domain import Rank
from err import RankAuthorizationResponderException
from transit import RankCarrier, RankAuthorizationDispatcher
from util import LoggingLevelRouter


class RankAuthorizationResponder(ModelAuthorizationResponder[Rank]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Rank authorization Request-Response workflow.

    Attributes:
        dispatcher: RankAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: RankAuthorizationRequest[T]) -> RankDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[RankAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[RankAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or RankAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> RankAuthorizationDispatcher:
        return cast(RankAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: RankAuthorizationRequest
    ) -> RankDecision:
        """
        Certify a candidate is a RankCarrier whose payload is either a Rank
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: RankAuthorizationRequest
        Result:
            RankDecision
        Raises:
            RankAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return RankDecision.failure(
                request=request,
                result=result,
                exception=RankAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankAuthorizationResponderException.MSG,
                    err_code=RankAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(RankCarrier, result.payload)
        return RankDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )