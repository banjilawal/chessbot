# src/logic/coord/service/microservice.py

"""
Module: logic.coord.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Union

from build.scalar import Scalar, ScalarService
from geometry.vector import Vector, VectorService
from logic.system import ComputationResult, IdFactory, IntegrityMicroservice
from logic.coord import Coord, CoordBuilder, CoordOpsController, CoordServiceException, CoordValidator


class CoordService(IntegrityMicroservice[Coord]):
    """
    Role:
        -   API
        -   Stateless microservice
        -   Lifecycle Manager
        -   Operations Provider

    Responsibilities:
        1.  Baremetal service request API for Coord operations.
        2.  Maintain the build-validation security lifecycle for Coord instances.

    Attributes:
        SERVICE_NAME: CoordService

        id: int
        schema: schema
        build: Coordbuild
        validation: CoordValidation
        controller: CoordOpsController

    Provides:
    
        -   euclidean_distance(u: Coord, v: Coord) -> ComputationResult[int]
        
        -   add_to_coord(
                    coord: Optional[Coord],
                    operand: Union[Vector, Coord],
                    vector_service: VectorService,
            ) -> ComputationResult[Coord]

        -   multiply_by_scalar(
                    coord: Coord,
                    scalar: Scalar,
                    scalar_service: ScalarService,
            ) -> ComputationResult[Coord]

        -   convert_vector_to_coord(
                    self,
                    vector: Vector,
                    vector_service: VectorService = VectorService()
            ) -> BuildResult[Coord]

    Super Class:
        IntegrityMicroservice
    """
    SERVICE_NAME = "CoordService"
    _ops_controller: CoordOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="CoordService"),
            ops_controller: CoordOpsController = CoordOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            ops_controller: CoordOpsController
        """
        super().__init__(id=id, name=name)
        self._ops_controller = ops_controller

    @property
    def builder(self) -> CoordBuilder:
        return self._ops_controller.build
    
    @property
    def validator(self) -> CoordValidator:
        return self._ops_controller.validation
    
    @property
    def ops_controller(self) -> CoordOpsController:
        return self._ops_controller
    
    def add_to_coord(
            self,
            coord: Coord,
            operand: Union[Vector, Coord],
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Coord]:
        """
        Add an operand to a coord.
        
        Actions:
            1.  Send an exception chain in the ComputationResult if either:
                    -   The coord is unsafe.
                    -   The operand is unsafe.
                    -   Their summation is not computed.
            2.  Otherwise, send the success result.
        Args:
            coord: [Coord]
            operand: Union[Vector, Coord]
            vector_service: VectorService
        Returns:
            ComputationResult[Coord]
        Raises:
            CoordServiceException
        """
        method = f"{self.__class__.__name__}.add_to_coord"
        
        # ServiceRequest a summation from the controller.
        request_result = self._ops_controller.arithmetic.addition.execute(
            coord=coord,
            operand=operand,
            coord_service=self,
            vector_service=vector_service,
        )
        # Handle the case that, the request is not fulfilled.
        if request_result.is_failure:
            return ComputationResult.failure(
                CoordServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordServiceException.MSG,
                    err_code=CoordServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
      
    def multiply_coord(
            self,
            coord: Coord,
            scalar: Scalar,
            scalar_service: ScalarService = ScalarService(),
    ) -> ComputationResult[Coord]:
        """
        Multiply a cord by a scalar.

        Actions:
            1.  Send an exception chain in the ComputationResult if either:
                    -   The coord is unsafe.
                    -   The scalar is unsafe.
                    -   Their product is not computed.
            2.  Otherwise, send the success result.
        Args:
            coord: [Coord]
            scalar: Scalar
            scalar_service: ScalarService
        Returns:
            ComputationResult[Coord]
        Raises:
            CoordServiceException
        """
        method = f"{self.__class__.__name__}.multiply_coord"
        
        # ServiceRequest a multiplication from the controller.
        request_result = self._ops_controller.arithmetic.multiplication.execute(
            coord=coord,
            scalar=scalar,
            coord_service=self,
            scalar_service=scalar_service,
        )
        # Handle the case that, the request is not fulfilled.
        if request_result.is_failure:
            return ComputationResult.failure(
                CoordServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordServiceException.MSG,
                    err_code=CoordServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
        
    def distance(self, u: Coord, v: Coord) -> ComputationResult[int]:
        """
        Find the distance between two coords.

        Actions:
            1.  Send an exception chain in the ComputationResult if either:
                    -   A coord is unsafe.
                    -   Their distance is not computed.
            2.  Otherwise, send the success result.
        Args:
            u: Coord
            v: Coord
        Returns:
            ComputationResult[Coord]
        Raises:
            CoordServiceException
        """
        method = f"{self.__class__.__name__}.distance"
        
        # ServiceRequest a multiplication from the controller.
        request_result = self._ops_controller.arithmetic.distance.compute(
            u=u,
            v=v,
            coord_service=self,
        )
        # Handle the case that, the request is not fulfilled.
        if request_result.is_failure:
            return ComputationResult.failure(
                CoordServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordServiceException.MSG,
                    err_code=CoordServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
    def convert_vector_to_coord(
            self,
            vector: Vector,
            vector_service: VectorService = VectorService()
    ) -> ComputationResult[Coord]:
        """
        Convert a vector to a coord.

        Actions:
            1.  Send an exception chain in the ComputationResult if either:
                    -   The vector is unsafe.
                    -   A coord cannot be built from the vector's components.
            2.  Otherwise, send the success result.
        Args:
            vector: Vector,
            vector_service: VectorService
        Returns:
            ComputationResult[Coord]
        Raises:
            CoordServiceException
        """
        method = f"{self.__class__.__name__}.convert_vector_to_coord"
        
        # ServiceRequest a conversion from the controller.
        request_result = self._ops_controller.arithmetic.conversion.execute(
            vector=vector,
            coord_service=self,
            vector_service=vector_service,
        )
        # Handle the case that, the request is not fulfilled.
        if request_result.is_failure:
            return ComputationResult.failure(
                CoordServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordServiceException.MSG,
                    err_code=CoordServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
