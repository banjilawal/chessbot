# src/exchange/responder/authorization/struct/node/warning/responder.py

"""
Module: exchange.responder.authorization.struct.node.warning.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, EncounterWaningNodeDecision
from domain import EncounterWaningNode
from exchange import NodeAuthorizationResponder, EncounterWaningNodePermissionRequest
from err import EncounterWaningNodeAuthorizationResponderException
from transit import WarningCarrier, EncounterWaningNodeCarrier, EncounterWaningNodeAuthorizationDispatcher
from util import LoggingLevelRouter


class EncounterWaningNodeAuthorizationResponder(NodeAuthorizationResponder[EncounterWaningNode]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the EncounterWaningNode authorization Request-Response workflow.

    Attributes:
        dispatcher: EncounterWaningNodeAuthorizationDispatcher[T]

    Provides:
        -   def execute(request: EncounterWaningNodePermissionRequest[T]) -> EncounterWaningNodeDecision[T]

    Super Class:
        NodeValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[EncounterWaningNodeAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[EncounterWaningNodeAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or EncounterWaningNodeAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> EncounterWaningNodeAuthorizationDispatcher:
        return cast(EncounterWaningNodeAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: EncounterWaningNodePermissionRequest
    ) -> EncounterWaningNodeDecision:
        """
        Certify a candidate is a WarningCarrier whose payload is either a Warning
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: EncounterWaningNodePermissionRequest
        Result:
            EncounterWaningNodeDecision
        Raises:
            WarningAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return EncounterWaningNodeDecision.failure(
                request=request,
                result=result,
                exception=EncounterWaningNodeAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterWaningNodeAuthorizationResponderException.MSG,
                    err_code=EncounterWaningNodeAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(EncounterWaningNodeCarrier, result.authorization_applicant)
        return EncounterWaningNodeDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )