# src/exchange/responder/fabrication/model/footstep/responder.py

"""
Module: exchange.responder.fabrication.model.footstep.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import FootstepBuildResponse, BuildResult
from domain import Footstep
from err import FootstepBuildResponderException
from exchange import FootstepBuildRequest, ModelBuildResponder
from transit import FootstepCarrier, FootstepBuildDispatcher
from util import LoggingLevelRouter


class FootstepBuildResponder(ModelBuildResponder[Footstep]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Footstep build Request-Response workflow.

    Attributes:
        dispatcher: FootstepBuildDispatcher[T]

    Provides:
        -   def submit(request: FootstepBuildRequest[T]) -> FootstepBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[FootstepBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[FootstepBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or FootstepBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> FootstepBuildDispatcher:
        return cast(FootstepBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: FootstepBuildRequest
    ) -> FootstepBuildResponse:
        """
        Certify a candidate is a CoordCarrier whose payload is either a Coord
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: FootstepBuildRequest
        Result:
            FootstepBuildResponse
        Raises:
            CoordValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return FootstepBuildResponse.failure(
                request=request,
                result=result,
                exception=FootstepBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepBuildResponderException.MSG,
                    err_code=FootstepBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(FootstepCarrier, result.payload)
        return FootstepBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )