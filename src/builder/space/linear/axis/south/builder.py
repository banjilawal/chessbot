from typing import Optional, cast

from builder import Builder
from model import Vector
from register import VectorRegister
from result import BuildResult

from space import SouthAxis, SouthAxisStepper

from util import LoggingLevelRouter
from validator import VectorValidator


class SouthAxisBuilder(Builder[SouthAxis]):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create an SouthAxis from the origin.

    Attributes:
        origin: Vector,
        stepper: Optional[AxisSouthAxisStepper]
        vector_validator: Optional[VectorValidator]

    Provides:
        -   def execute() -> BuildResult[SouthAxis]

    Super Class:
    """
    _origin: Vector
    _stepper: SouthAxisStepper
    _vector_validator: VectorValidator
    
    def __init__(
            self,
            origin: Vector,
            stepper: Optional[SouthAxisStepper] | None = SouthAxisStepper(),
            vector_validator: Optional[VectorValidator] | None = VectorValidator(),
    ):
        """
        Args:
            origin: Vector,
            stepper: Optional[AxisSouthAxisStepper]
            vector_validator: Optional[VectorValidator]
        """
        self._origin = origin
        self._stepper = stepper
        self._vector_validator = vector_validator
     
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[SouthAxis]:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the origin is flagged unsafe.
        validation = self._vector_validator.execute(canidate=self._origin)
        if validation.is_failure:
            # Handle the case that the request is not satisfied.
            if validation.is_failure:
                # Send the exception in the result.
                return BuildResult.failure(
                    SouthAxisBuilderException(
                        cls_mth=method,
                        cls_name=self.__class__.__name__,
                        msg=SouthAxisBuilderException.MSG,
                        err_code=SouthAxisBuilderException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.BUILD_RESULT,
                        ex=validation.exception
                    )
                )
        origin = cast(Vector, validation.payload)
        
        # Request a register of the endpoints.
        endpoint_request = SouthAxisEndpointBuilder(
            origin=self._origin,
        ).execute()
        # Handle the case that the request is not satisfied.
        if endpoint_request.is_failure:
            # Send the exception in the result.
            return BuildResult.failure(
                SouthAxisBuilderException(
                    cls_mth=method,
                    cls_name=self.__class__.__name__,
                    msg=SouthAxisBuilderException.MSG,
                    err_code=SouthAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=endpoint_request.exception
                )
            )
        # Otherwise, extract and cast the product.
        endpoints = cast(VectorRegister, endpoint_request.payload)
        axis = SouthAxis(endpoints=endpoints, stepper=self._stepper)

        return BuildResult.success(axis)