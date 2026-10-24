# src/artifact/response/deletion/struct/register/coord/response.py

"""
Module: artifact.response.deletion.struct.register.coord.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import RegisterDeletionResponse, ResponseState, DeletionResult
from exchange import Request, CoordRegisterDeletionRequest
from domain import CoordRegister, CoordRegisterBlueprint
from transit import CoordRegisterCarrier


class CoordRegisterDeletionResponse(
    RegisterDeletionResponse[CoordRegister]
):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a CoordRegister deletion request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: DeletionResult[CoordRegisterCarrier]
        request: CoordRegisterDeletionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Coord]
        -   def valid_blueprint() -> Optional[CoordRegisterBlueprint]

        -   def success(
                    request: Request,
                    result: DeletionResult[CoordRegisterCarrier],
            ) -> CoordRegisterDeletionResponse

        -   def failure(
                    request: Request,
                    result: DeletionResult[CoordRegisterCarrier],
                    exception: Exception,
            ) -> CoordRegisterDeletionResponse
            
    Super Class:
        RegisterDeletionResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: DeletionResult,
            request: CoordRegisterDeletionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: DeletionResult[CoordRegisterCarrier]
            request: CoordRegisterDeletionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
    
    @property
    def request(self) -> CoordRegisterDeletionRequest:
        return cast(CoordRegisterDeletionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[CoordRegister]:
        # Handle the case that the deletion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(CoordRegisterCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, CoordRegisterCarrier)
        ):
            return None
        # Handle the case that there is no register in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the register. ---#
        register = cast(CoordRegister, carrier.entity)
        # Handle the case that the register is null or the wrong type.
        if (
                register is None or
                not isinstance(register, CoordRegister)
        ):
            return None
        # Finally send the success result.
        return register
    
    @property
    def valid_blueprint(self) -> Optional[CoordRegisterBlueprint]:
        # Handle the case that the deletion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(CoordRegisterCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, CoordRegisterCarrier)
        ):
            return None
        # Handle the case that there is no blueprint in the carrier.
        if not carrier.has_blueprint:
            return None
        # --- Extract the blueprint. ---#
        blueprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null or the wrong type.
        if (
                blueprint is None or
                not isinstance(blueprint, CoordRegisterBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: DeletionResult,
    ) -> CoordRegisterDeletionResponse:
        # Downcast the request into a CoordRegisterDeletionRequest.
        deletion_request = cast(
            CoordRegisterDeletionRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=deletion_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: DeletionResult,
            exception: Exception,
    ) -> CoordRegisterDeletionResponse:
        # Downcast the request into a CoordRegisterDeletionRequest.
        deletion_request = cast(
            CoordRegisterDeletionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=deletion_request,
            state=ResponseState.FAILURE,
        )