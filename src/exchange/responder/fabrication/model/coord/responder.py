# src/exchange/responder/fabrication/model/coord/responder.py

"""
Module: exchange.responder.fabrication.model.coord.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, CoordBuildResponse
from exchange import ModelBuildResponder, CoordBuildRequest
from domain import Coord
from err import CoordBuildResponderException
from transit import CoordCarrier, CoordBuildDispatcher
from util import LoggingLevelRouter


class CoordBuildResponder(ModelBuildResponder[Coord]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Coord build Request-Response workflow.

    Attributes:
        dispatcher: CoordBuildDispatcher[T]

    Provides:
        -   def submit(request: CoordBuildRequest[T]) -> CoordBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[CoordBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[CoordBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or CoordBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> CoordBuildDispatcher:
        return cast(CoordBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: CoordBuildRequest
    ) -> CoordBuildResponse:
        """
        Certify a candidate is a CoordCarrier whose payload is either a Coord
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: CoordBuildRequest
        Result:
            CoordBuildResponse
        Raises:
            CoordValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return CoordBuildResponse.failure(
                request=request,
                result=result,
                exception=CoordBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordBuildResponderException.MSG,
                    err_code=CoordBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(CoordCarrier, result.payload)
        return CoordBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )