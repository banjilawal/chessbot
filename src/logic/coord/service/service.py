# src/logic/coord/service/compute.py

"""
Module: logic.coord.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations
from math import sqrt
from typing import cast

from logic.scalar import Scalar, ScalarService
from logic.vector import Vector, VectorService
from logic.coord import Coord, CoordBuildProcess, CoordOpsController, CoordServiceException, CoordValidationProcess
from logic.system import BuildResult, ComputationResult, IdFactory, IntegrityService, id_emitter

class CoordService(IntegrityService[Coord]):
    """
    Role:Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Coord microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Coord state by providing single entry and exit points to Coord
        lifecycle.

    Super Class:
        *   IntegrityService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
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
    def build(self) -> CoordBuildProcess:
        return self._ops_controller.build
    
    @property
    def validation(self) -> CoordValidationProcess:
        return self._ops_controller.validation
    
    @property
    def ops_controller(self) -> CoordOpsController:
        return self._ops_controller
    
    def add_vector_to_coord(
            self,
            coord: Coord,
            vector: Vector,
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Coord]:
        """
        # ACTION:
        1.  Certify the vector argument with vector_service.
        2.  Certify the coord argument with the service's validation.
        3.  Get the new row and column using the expression
                    new_row, new_colum = coord.row + vector.y, coord.column + vector.x
        5.  Using the service's CoordBuildProcess instance create and return the new Coord.

        # PARAMETERS:
            *   coord(Coord)
            *   vector (Vector)
            *   vector_service (VectorService)

        # RETURNS:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        RAISES:
            *   CoordServiceException
        """
        method = f"{self.__class__.__name__}.add_vector_to_coord"
        
        return self._ops_controller.arithmetic.add_vector_to_coord.compute(
            coord=coord,
            vector=vector,
            coord_service=self,
            vector_service=vector_service,
        )
      
    def multiply_coord_by_scalar(
            self,
            coord: Coord,
            scalar: Scalar,
            scalar_service: ScalarService = ScalarService(),
    ) -> BuildResult[Coord]:
        """
        # ACTION:
        1.  Certify the vector argument with vector_service.
        2.  Certify the coord argument with the service's validation.
        3.  Get the new row and column using the expression
                    new_row, new_colum = coord.row * scalar.value, coord.column + scalar.value
        5.  Using the service's CoordBuildProcess instance create and return the new Coord.

        # PARAMETERS:
            *   coord(Coord)
            *   scalar (Scalar)
            *   scalar_service (ScalarService)
            *   not_negative_validator (NotNegativeNumberValidator)

        # RETURNS:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        RAISES:
            *   CoordServiceExceptio
        """
        method = f"f{self.__class__.__name__}.multiply_coord_by_scalar"
        
        return self._osp.arithmetic.multiply_coord_by_scalar.compute(
            coord=coord,
            scalar=scalar,
            coord_service=self,
            scalar_service=scalar_service,
        )
        
    def euclidean_distance(self, u: Coord, v: Coord) -> ComputationResult[int]:
        method = f"{self.__class__.__name__}.euclidean_distance"
        
        return self._ops_controller.arithmetic.euclidean_distance.compute(
            u=u,
            v=v,
            coord_service=self,
        )
    
    def convert_vector_to_coord(
            self,
            vector: Vector,
            vector_service: VectorService = VectorService()
    ) -> ComputationResult[Coord]:
        """
        # ACTION:
        1.  vector_service runs integrity checks on param.
        2.  If any checks raise an exception return it in the BuildResult.
        3.  Run build_coord(row=y, column=y) to ensure the computed values produce a
            safe Coord instance.

        # PARAMETERS:
            *   vector (Vector)
            *   vector_service (VectorService)

        # RETURNS:
        BuildResult[Coord] containing either:
            - On success: Coord in the payload.
            - On failure: Exception.

        RAISES:
            *   CoordServiceException
        """
        method = f"{self.__class__.__name__}.convert_vector_to_coord"
        
        return self._ops_controller.arithmetic.convert_vector_to_coord.compute(
            vector=vector,
            vector_service=vector_service,
            coord_service=self,
        )
    
