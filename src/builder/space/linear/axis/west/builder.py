from typing import Optional, cast

from builder import Builder
from model import Vector
from register import VectorRegister
from result import BuildResult

from space import WestAxis, WestAxisStepper

from util import LoggingLevelRouter
from validator import VectorValidator


class WestAxisBuilder(Builder[WestAxis]):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create an WestAxis from the origin.

    Attributes:
        origin: Vector,
        stepper: Optional[AxisWestAxisStepper]
        vector_validator: Optional[VectorValidator]

    Provides:
        -   def execute() -> BuildResult[WestAxis]

    Super Class:
    """
    _origin: Vector
    _stepper: WestAxisStepper
    _vector_validator: VectorValidator
    
    def __init__(
            self,
            origin: Vector,
            stepper: Optional[WestAxisStepper] | None = WestAxisStepper(),
            vector_validator: Optional[VectorValidator] | None = VectorValidator(),
    ):
        """
        Args:
            origin: Vector,
            stepper: Optional[AxisWestAxisStepper]
            vector_validator: Optional[VectorValidator]
        """
        self._origin = origin
        self._stepper = stepper
        self._vector_validator = vector_validator
     
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[WestAxis]:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the origin is flagged unsafe.
        validation = self._vector_validator.execute(canidate=self._origin)
        if validation.is_failure:
            # Handle the case that the request is not satisfied.
            if validation.is_failure:
                # Send the exception in the result.
                return BuildResult.failure(
                    WestAxisBuilderException(
                        cls_mth=method,
                        cls_name=self.__class__.__name__,
                        msg=WestAxisBuilderException.MSG,
                        err_code=WestAxisBuilderException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.BUILD_RESULT,
                        ex=validation.exception
                    )
                )
        origin = cast(Vector, validation.payload)
        
        # Request a register of the endpoints.
        endpoint_request = WestAxisEndpointBuilder(
            origin=self._origin,
        ).execute()
        # Handle the case that the request is not satisfied.
        if endpoint_request.is_failure:
            # Send the exception in the result.
            return BuildResult.failure(
                WestAxisBuilderException(
                    cls_mth=method,
                    cls_name=self.__class__.__name__,
                    msg=WestAxisBuilderException.MSG,
                    err_code=WestAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=endpoint_request.exception
                )
            )
        # Otherwise, extract and cast the product.
        endpoints = cast(VectorRegister, endpoint_request.payload)
        axis = WestAxis(endpoints=endpoints, stepper=self._stepper)

        return BuildResult.success(axis)