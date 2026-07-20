from typing import cast

from bootstrapper import VectorAssemblyPrimer
from builder import AxisEndpointFactory
from register import VectorRegister
from result import BuildResult
from schema import AxisOrientation
from space import EastAxisStepper
from space.cateoory.linear.axis.east import EastAxis
from util import LoggingLevelRouter


class EastAxisBuilder(Builder[EastAxis]):
    _origin: Vector
    _orientation: AxisOrientation
    _endpoint_factory: AxisEndpointFactory
    _stepper_factory: AxisStepperFactory
    _vector_validator: VectorValidator
    
    def __init__(
            self,
            origin: Vector,
            orientation: Optional[AxisOrientation] | None = AxisOrientation.EAST,
            endpoint_factory: Optional[AxisEndpointFactory] | None = AxisEndpointFactory(),
            stepper_factory: Optional[StepperFactory] | None = AxisStepperFactory(),
            vector_validator: Optional[VectorValidator] | None = VectorValidator(),
    ):
        """
        Args:
            origin: Vector,
            orientation: Optional[AxisOrientation]
            endpoint_factory: Optional[AxisEndpointFactory]
            stepper_factory: Optional[AxisStepperFactory]
            vector_validator: Optional[VectorValidator]
        """
        self._origin = origin
        self._origin = orientation
        self._endpoint_factory = endpoint_factory
        self._stepper_factory = stepper_factory
        self._vector_validator = vector_validator
        
        
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[EastAxis]:
        
        endpoint_build = AxisEndpointFactory(
            origin=self._origin, 
            orientation=self._orientation
        ).execute()
        if endpoint_build.is_failure:
            return BuildResult.failure(
                EastAxisBuilderException(
                    cls_mth=method,
                    cls_name=self.__class__.__name__,
                    msg=EastAxisBuilderException.MSG,
                    err_code=EastAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=endpoint_build.exception
                )
            )
        endpoints = cast(VectorRegister, endpoint_build.payload)
        
        stepper_build = StepperFactory(orientation=orientation).execute()
        if endpoint_build.is_failure:
            return BuildResult.failure(
                EastAxisBuilderException(
                    cls_mth=method,
                    cls_name=self.__class__.__name__,
                    msg=EastAxisBuilderException.MSG,
                    err_code=EastAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=stepper_build.exception
                )
            )
        stepper = cast(EastAxisStepper, stepper_build.payload)
        
        axis = EastAxis(endpoints=endpoints, stepper=stepper)
        return BuildResult.success(axis)