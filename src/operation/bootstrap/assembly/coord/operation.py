# src/operation/bootstrap/assembly/coord/operation.py

"""
Module: operation.bootstrap.assembly.coord.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Coord, CoordBlueprint
from operation import AssemblyBootstrapper
from result import ValidationResult
from system import BOARD_DIMENSION, LoggingLevelRouter
from toolkit import MathToolkit


class CoordAssemblyBootstrapper(AssemblyBootstrapper[Coord]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner
    
    Responsibilities:
        1.  Ensure a new Coord instance is born safe and reliable.
    
    Attributes:
    
    Provides:
        -   def execute(
                blueprint: CoordBlueprint,
                toolkit: MathToolkit,
        ) -> ValidationResult[CoordBlueprint]:
    
    Super Class:
        AssemblyBootstrapper
     """
    @classmethod
    @LoggingLevelRouter.monitor()
    def execute(
            cls,
            blueprint: CoordBlueprint,
            toolkit: MathToolkit | None = None,
    ) -> ValidationResult[CoordBlueprint]:
        """
        Action:
            1.  Send an exception chain in the ValidationResult if
                    -   Any build param fails does not pass a validation check.
                    -   The coord's attributes have already been used on the board.
            2.  Build the Coord instance with the params.
            3.  Send an exception chain in the ValidationResult if
                    * The coord requires insertion into the board but the insertion fails.
            4.  Return the Coord instance in the ValidationResult.
        Args:
            blueprint: CoordBlueprint
            toolkit: CoordToolkit
        Returns:
            ValidationResult[CoordBlueprint]
        Raises:
            CoordBuildException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        if toolkit is None:
            toolkit = MathToolkit()
        
        # Handle the case that, either component is out of bounds.
        for num in [blueprint.x, blueprint.y]:
            validation_result = toolkit.number_validator.validate(
                floor=0,
                ceiling=BOARD_DIMENSION / 2,
                candidate=abs(num)
            )
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    CoordAssemblyBootstrapperException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=CoordAssemblyBootstrapperException.MSG,
                        err_code=CoordAssemblyBootstrapperException.ERR_CODE,
                        ex=validation_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(blueprint)
