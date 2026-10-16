# src/exchange/responder/fabrication/struct/node/warning/responder.py

"""
Module: exchange.responder.fabrication.struct.node.warning.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, EncounterWaningNodeBuildResponse
from domain import EncounterWaningNode
from exchange import NodeBuildResponder, EncounterWaningNodeBuildRequest
from err import EncounterWaningNodeBuildResponderException
from transit import WarningCarrier, EncounterWaningNodeCarrier, EncounterWaningNodeBuildDispatcher
from util import LoggingLevelRouter


class EncounterWaningNodeBuildResponder(NodeBuildResponder[EncounterWaningNode]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the EncounterWaningNode build Request-Response workflow.

    Attributes:
        dispatcher: EncounterWaningNodeBuildDispatcher[T]

    Provides:
        -   def submit(request: EncounterWaningNodeBuildRequest[T]) -> EncounterWaningNodeBuildResponse[T]

    Super Class:
        NodeValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[EncounterWaningNodeBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[EncounterWaningNodeBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or EncounterWaningNodeBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> EncounterWaningNodeBuildDispatcher:
        return cast(EncounterWaningNodeBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: EncounterWaningNodeBuildRequest
    ) -> EncounterWaningNodeBuildResponse:
        """
        Certify a candidate is a WarningCarrier whose payload is either a Warning
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: EncounterWaningNodeBuildRequest
        Result:
            EncounterWaningNodeBuildResponse
        Raises:
            WarningValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return EncounterWaningNodeBuildResponse.failure(
                request=request,
                result=result,
                exception=EncounterWaningNodeBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWaningNodeBuildResponderException.MSG,
                    err_code=EncounterWaningNodeBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(EncounterWaningNodeCarrier, result.payload)
        return EncounterWaningNodeBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )