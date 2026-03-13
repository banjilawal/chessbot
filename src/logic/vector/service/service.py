# src/logic/vector/service.py

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
from logic.vector import Vector, VectorBuilder, VectorServiceException, VectorValidator
from logic.system import (
    BuildResult, ComputationResult, IdFactory, LoggingLevelRouter, IntegrityService,  NumberValidator
)

class VectorService(IntegrityService[Vector]):
    """
    # LOCAL ROLE:
        Computation, Transformer
    
    # INHERITED ROLE:
        *   See IntegrityService class for inherited role.
    
    # LOCAL RESPONSIBILITIES:
    1.  Creating new Vector objects by scalar multiplication.
    2.  Converting a Vector into a Coord.
    
    # INHERITED RESPONSIBILITIES:
        *   See IntegrityService class for inherited responsibilities.

    # PARENT:
        *   IntegrityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   SERVICE_NAME (str)

    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   id (int)
        *   name (str)
        *   builder (VectorBuilder) = VectorBuilder()
        *   validator (VectorValidator) = VectorValidator()

    # LOCAL METHODS:
        *   multiply_vector_by_scalar(
                    vector: Vector,
                    scalar: Scalar,
                    scalar_service: ScalarService = ScalarService()
            ) -> ComputationResult[Vector]
            
        *   convert_coord_to_vector(
                coord: Coord,
                coord_service: CoordService = CoordService(),
            ) -> BuildResult[Vector]:

    # INHERITED METHODS:
        *   See IntegrityService class for inherited methods.
    """
    SERVICE_NAME = "VectorService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: VectorBuilder = VectorBuilder(),
            validator: VectorValidator = VectorValidator(),
            id: int = IdFactory.next_id(class_name="VectorService"),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> VectorBuilder:
        """get VectorBuilder"""
        return cast(VectorBuilder, self.entity_builder)
    
    @property
    def validator(self) -> VectorValidator:
        """get VectorValidator"""
        return cast(VectorValidator, self.entity_validator)
    
    @LoggingLevelRouter.monitor
    def add_vectors(
            self,
            vectors: List[Vector],
            number_validator: NumberValidator = NumberValidator(),
    ) -> ComputationResult[Vector]:
        """
        Action:
            1.  Return an exception chain in the ComputationResult if
                    * Any item in the list fails its validation checks.
            2.  Iterate through the vectors, adding them to an accumulator. Send an exception
                chain in the ComputationResult if
                    * any of the accumulations is out of bounds
            3.  When the loop finishes return the work product.

        Args:
            vectors: List[Vector]
            number_validator: NumberValidator

        Returns:
            ComputationResult[Vector]

        Raises:
            VectorServiceException
        """
        method = f"{self.__class__.__name__}.add_vectors"
        
        # Handle the case that, one of the vectors in not certified as safe
        for vector in vectors:
            validation_result = self.validator.validate(candidate=vector)
            if validation_result.is_failure:
                # Send an exception chain on failure.
                return ComputationResult.failure(
                    VectorServiceException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorServiceException.MSG,
                        err_code=VectorServiceException.ERR_CODE,
                        ex=validation_result.exception,
                    )
                )
        # --- Create the return target ---#
        sum = Vector(x=0, y=0)
        
        for vector in vectors:
            summation_result = self.builder.build(
                x=sum.x + vector.x,
                y=sum.y + vector.y,
                number_validator=number_validator,
            )
            # Handle the case that, the summation does not produce a work product.
            if summation_result.is_failure:
                return ComputationResult.failure(
                    VectorServiceException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorServiceException.MSG,
                        err_code=VectorServiceException.ERR_CODE,
                        ex=summation_result.exception,
                    )
                )
            # --- Update the accumulation. ---#
            sum = summation_result.payload
        
        # --- Send the work product in the ComputationResult. ---#
        return ComputationResult.success(sum)
    
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
                    *   The vector is not certified as safe.
                    *   The scalar is not certified as safe.
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
        
        # Handle the case that, the vector is not certified as safe.
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
        # Handle the case that, the scalar is not certified as safe.
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
                    *   The coord is not certified as safe.
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
        
        # Handle the case that, the coord is not certified as safe.
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
    