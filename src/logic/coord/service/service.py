# src/logic/coord/service/process.py

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
from logic.coord import Coord, CoordBuildProcess, CoordServiceException, CoordValidationProcess
from logic.system import BuildResult, ComputationResult, IntegrityService, id_emitter

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
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: CoordBuildProcess = CoordBuildProcess(),
            validator: CoordValidationProcess = CoordValidationProcess(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   build (CoordFactory)
            *   validation (CoordValidationProcess)

        # RETURNS:
        None

        Raises:
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)

    @property
    def build(self) -> CoordBuildProcess:
        """get CoordBuildProcess"""
        return cast(CoordBuildProcess, self.entity_builder)
    
    @property
    def validation(self) -> CoordValidationProcess:
        """get CoordValidationProcess"""
        return cast(CoordValidationProcess, self.entity_validator)
    
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
        method = "CoordService.add_vector_to_coord"
        try:
            # Certify the coord param
            coord_validation = self._validator.execute(candidate=coord)
            if coord_validation.is_failure:
                return BuildResult.failure(coord_validation.exception)
            # Certify the vector param.
            vector_validation = vector_service.validation.execute(candidate=vector)
            if vector_validation.is_failure:
                return BuildResult.failure(vector_validation.exception)
            
            # when params are certified return the BuildResult.
            build_result =  self.build.execute(
                row=(coord.row + vector.y), column=(coord.column + vector.x), validator=self.validation
            )
            if build_result.is_failure:
                return ComputationResult.failure(build_result.exception)
            return ComputationResult.success(build_result.payload)
        # Finally, catch any missed exception and wrap A CoordServiceException around it then return the
        # exception-chain inside the BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                CoordServiceException(ex=ex, msg= f"{method}: {CoordServiceException.MSG}")
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
            *   CoordServiceException
        """
        method = "CoordService.multiply_coord_by_scalar"
        try:
            # Certify the coord param
            coord_validation = self._validator.execute(candidate=coord)
            if coord_validation.is_failure:
                return BuildResult.failure(coord_validation.exception)
            # Certify the scalar param
            scalar_validation = scalar_service.validation.execute(candidate=scalar)
            if scalar_validation.is_failure:
                return BuildResult.failure(scalar_validation.exception)
            
            # when params are certified return the BuildResult.
            return self._builder.execute(
                row=(coord.y * scalar.value), column=(coord.x * scalar.value), validator=self.validation
            )
            # Finally, catch any missed exception and wrap A CoordServiceException around it then return the
            # exception-chain inside the BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                CoordServiceException(ex=ex, msg=f"{method}: {CoordServiceException.MSG}")
            )
        
    def euclidean_distance(self, u: Coord, v: Coord) -> ComputationResult[int]:
        method = "CoordService.euclidean_distance"
        
        # Handle the case that, the u does not pass a validation check.
        u_validation = self._validator.execute(candidate=u)
        if u_validation.is_failure:
            return ComputationResult.failure(u_validation.exception)
        
        # Handle the case that, v does not pass a validation check.
        v_validation = self._validator.execute(candidate=v)
        if v_validation.is_failure:
            return ComputationResult.failure(v_validation.exception)
        
        # Compute the Euclidean distance and return it.
        distance = sqrt(pow(base=(u.row - v.row), exp=2) + pow(base=(u.column - v.column), exp=2))
        return ComputationResult.success(payload=cast(int, distance))
        
    
    def convert_vector_to_coord(
            self,
            vector: Vector,
            vector_service: VectorService = VectorService()
    ) -> BuildResult[Coord]:
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
        method = "CoordService.convert_vector_to_coord"
        try:
            # Certify the vector param
            vector_validation = vector_service.validation.execute(candidate=vector)
            if vector_validation.is_failure:
                return BuildResult.failure(vector_validation.exception)
            # After the vector is certified return the BuildResult.
            return self._builder.execute(row=vector.y, column=vector.x, validator=self.validation
                                         )
            # Finally, catch any missed exception and wrap A CoordServiceException around it then return the
            # exception-chain inside the BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                CoordServiceException(ex=ex, msg=f"{method}: {CoordServiceException.MSG}")
            )
    
