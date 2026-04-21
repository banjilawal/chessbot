# src/operation/bootstrap/assembly/coord/operation.py

"""
Module: operation.bootstrap.assembly.coord.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import BootstrapCoordAssemblyException
from toolkit import MathToolkit
from result import ValidationResult
from model import Coord, CoordBlueprint
from operation import AssemblyBootstrapper
from system import BOARD_DIMENSION, LoggingLevelRouter


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
            1.  Send an exception chain in the ValidationResult if either component fails a
                validation check.
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
        for component in [blueprint.x, blueprint.y]:
            validation_result = toolkit.number_validator.validate(
                floor=0,
                ceiling=BOARD_DIMENSION / 2,
                candidate=abs(component)
            )
            if validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    BootstrapCoordAssemblyException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=BootstrapCoordAssemblyException.MSG,
                        err_code=BootstrapCoordAssemblyException.ERR_CODE,
                        ex=validation_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(blueprint)
