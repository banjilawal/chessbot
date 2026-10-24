# src/exchange/responder/fabrication/model/maneuver/responder.py

"""
Module: exchange.responder.fabrication.model.maneuver.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, ManeuverBuildResponse
from exchange import ModelBuildResponder, ManeuverBuildRequest
from domain import Maneuver
from err import ManeuverBuildResponderException
from transit import ManeuverCarrier, ManeuverBuildDispatcher
from util import LoggingLevelRouter


class ManeuverBuildResponder(ModelBuildResponder[Maneuver]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Maneuver build Request-Response workflow.

    Attributes:
        dispatcher: ManeuverBuildDispatcher[T]

    Provides:
        -   def execute(request: ManeuverBuildRequest[T]) -> ManeuverBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[ManeuverBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ManeuverBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ManeuverBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> ManeuverBuildDispatcher:
        return cast(ManeuverBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ManeuverBuildRequest
    ) -> ManeuverBuildResponse:
        """
        Certify a candidate is a ManeuverCarrier whose payload is either a Maneuver
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: ManeuverBuildRequest
        Result:
            ManeuverBuildResponse
        Raises:
            ManeuverValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return ManeuverBuildResponse.failure(
                request=request,
                result=result,
                exception=ManeuverBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverBuildResponderException.MSG,
                    err_code=ManeuverBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(ManeuverCarrier, result.payload)
        return ManeuverBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )