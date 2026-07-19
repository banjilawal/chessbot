from bootstrapper import VectorAssemblyPrimer
from builder import AxisEndpointFactory
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
    
    def __init__(
            self,
            origin: Vector,
            orientation: Optional[AxisOrientation] | None = AxisOrientation.EAST,
            endpoint_factory: Optional[AxisEndpointFactory] | None = AxisEndpointFactory(),
            stepper_factory: Optional[StepperFactory] | None = AxisStepperFactory(),
    ):
        """
        Args:
            origin: Vector,
            orientation: Optional[AxisOrientation]
            endpoint_factory: Optional[AxisEndpointFactory]
            stepper_factory: Optional[AxisStepperFactory]            
        """
        self._origin = origin
        self._origin = orientation
        self._endpoint_factory = endpoint_factory
        self._stepper_factory = stepper_factory
        
        
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
        
        stepper_build = SteperFactory(orientation=orientation).execute()
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