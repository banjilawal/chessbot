# src/logic/vector/validator.py

"""
Module: logic.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations
from typing import List, cast

from logic.coord import Coord, CoordService
from logic.scalar import Scalar, ScalarService
from logic.system.worker import Worker
from logic.vector import Vector, VectorBuilder, VectorService, VectorServiceException, VectorValidator
from logic.system import (
    BuildResult, ComputationResult, IdFactory, LoggingLevelRouter, IntegrityMicroservice, NumberValidator
)
from logic.vector.service.operation.arithmetic.convert.direction import ConversionDirection


class VectorCoordConverter(Worker):
    """
    Role:
        -   Worker
        -   Transformer

    Responsibilities:
        1.  Bidirectional Coord<->Vector converter.

    Attributes:

    Properties:
        -   def work(
                    coord
                    vector: Vector,
                    coor
                    vector_service: VectorService = VectorService(),
                    number_validator: NumberValidator = NumberValidator(),
            ) -> ComputationResult[Vector]

    Super Class:
        Worker
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def work(
            cls,
            coord: Coord,
            vector: Vector,
            conversion_direction: ConversionDirection,
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Vector]:
        method = f"{cls.__name__}.work"
        
        
    @LoggingLevelRouter.monitor
    def multiply_vector_by_scalar(
            self,
            vector: Vector,
            scalar: Scalar,
            scalar_service: ScalarService = ScalarService(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> ComputationResult[Vector]:
        """
        Action:
            
            1.  Return an exception chain in the ComputationResult if, either
                    *   The vector does not pass a validation check.
                    *   The scalar does not pass a validation check.
            2.  Using scalar c, and vector v, create vector p.
                    p = (v.x * c), (v.y * c)
            3.  If p does not satisfy the system's vector contract send an
                exception chain in the ComputationResult.
            4.  Otherwise, return the work product.
            
        Args:
            vector: Vector
            scalar: Scalar
            scalar_service: ScalarService
            number_validator: NumberValidator
            
        Returns:
            ComputationResult[Vector]
            
        Raises:
            VectorServiceException
        """
        method = f"{self.__class__.__name__}.multiply_vector_by_scalar"
        
        # Handle the case that, the vector does not pass a validation check.
        vector_validation_result = self.validator.validate(candidate=vector)
        if vector_validation_result.is_failure:
            # Send an exception chain on failure.
            return ComputationResult.failure(
                VectorServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorServiceException.MSG,
                    err_code=VectorServiceException.ERR_CODE,
                    ex=vector_validation_result.exception,
                )
            )
        # Handle the case that, the scalar does not pass a validation check.
        scalar_validation_result = scalar_service.validator.validate(candidate=scalar)
        if scalar_validation_result.is_failure:
            # Send an exception chain on failure.
            return ComputationResult.failure(
                VectorServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorServiceException.MSG,
                    err_code=VectorServiceException.ERR_CODE,
                    ex=scalar_validation_result.exception,
                )
            )
        # Handle the case that, the new build is unsuccessful.
        build_result = self.builder.build(
            x=vector.x * scalar,
            y=vector.y * scalar,
            number_validator=number_validator,
        )
        if build_result.is_failure:
            # Send an exception chain on failure.
            return ComputationResult.failure(
                VectorServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorServiceException.MSG,
                    err_code=VectorServiceException.ERR_CODE,
                    ex=build_result.exception,
                )
            )
        # --- Send the work product. ---#
        return ComputationResult.success(build_result.payload)
    
    @LoggingLevelRouter.monitor
    def convert_coord_to_vector(
            self,
            coord: Coord,
            coord_service: CoordService = CoordService(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> BuildResult[Vector]:
        """
        Action:
            1.  Send an exception chain in the BuildResult if, either
                    *   The coord does not pass a validation check.
                    *   The coord's attributes don't meet Vector specs.
            2.  Otherwise, return the work product.

        Args:
            coord: Coord
            coord_service: CoordService
            number_validator: NumberValidator

        Args:
            BuildResult[Vector]

        Raises:
            VectorServiceException
        """
        method = f"{self.__class__.__name__}.convert_coord_to_vector"
        
        # Handle the case that, the coord does not pass a validation check.
        coord_validation_result = coord_service.validator.validate(candidate=coord)
        if coord_validation_result.is_failure:
            # Send an exception chain on failure.
            return ComputationResult.failure(
                VectorServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorServiceException.MSG,
                    err_code=VectorServiceException.ERR_CODE,
                    ex=coord_validation_result.exception,
                )
            )
        vector_build_result = self.builder.build(
            x=coord.column,
            y=coord.row,
            number_validator=number_validator,
        )
        # Handle the case that, the build does not produce a work product.
        if vector_build_result.is_failure:
            # Send an exception chain on failure.
            return ComputationResult.failure(
                VectorServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorServiceException.MSG,
                    err_code=VectorServiceException.ERR_CODE,
                    ex=vector_build_result.exception,
                )
            )
        # --- Forward the work product. ---#
        return vector_build_result
    