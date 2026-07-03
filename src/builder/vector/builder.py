# src/builder/vector/builder.py

"""
Module: builder.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from system import (
    Builder, BuildResult, LONGEST_KNIGHT_LEG_SIZE, LoggingLevelRouter, NumberValidator
)
from model.math.vector import Vector, VectorBuilderException


class VectorBuilder(Builder[Vector]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner
        
   Responsibilities:
        1.  Ensure a new Vector instance is born safe and reliable.
    
    Attributes:
    
    Provides:
        -   def execute(
                x: int,
                y: int,
                number_validator: NumberValidator,
            ) -> BuildResult[Vector]
    
     Super Class:
         Builder
     """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            x: int,
            y: int,
            number_validator: NumberValidator = NumberValidator(),
    ) -> BuildResult[Vector]:
        """
        Build a safe Vector.

        Action:
            1.  Send an exception chain in the BuildResult if either x or y
                fail a bounds check.
            2.  Otherwise, build the Vector
            3.  Send the success result.
        Args:
            x: int
            y: int
            number_validator: NumberValidator
        Returns:
            BuildResult[Vector]
        Raises:
            VectorBuilderException
        """
        method = f"{cls.__name__}.build"
        
        # Handle the case that, either component is out of bounds.
        for num in [x, y]:
            validation_result = number_validator.build(
                floor=0,
                ceiling=LONGEST_KNIGHT_LEG_SIZE,
                candidate=abs(num)
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    VectorBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=VectorBuilderException.OP,
                        msg=VectorBuilderException.MSG,
                        err_code=VectorBuilderException.ERR_CODE,
                        mthd_rslt_type=VectorBuilderException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(Vector(x=x, y=y))