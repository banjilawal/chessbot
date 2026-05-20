# src/operation/priming/assembly/vector/operation.py

"""
Module: operation.priming.assembly.vector.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from setting import BoardDimensionSetting, BoardProperty
from controller import WorkerRegistryController
from toolkit import MathToolkit
from result import ValidationResult
from model import Vector, VectorBlueprint
from operation import AssemblyPrimer
from err import VectorAssemblyPrimingException
from util import LoggingLevelRouter


class VectorAssemblyPrimer(AssemblyPrimer[Vector]):
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
                    blueprint: VectorBlueprint,
                    toolkit: MathToolkit,
            ) -> ValidationResult[VectorBlueprint]:
    
    Super Class:
        AssemblyPrimingper
     """
    NAME = "vector_assembly_primingper"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            blueprint: VectorBlueprint,
            toolkit: MathToolkit | None = None,
    ) -> ValidationResult[VectorBlueprint]:
        """
        Action:
            1.  Send an exception chain in the ValidationResult if
                    -   Any build param fails does not pass a validation check.
                    -   The vector's attributes have already been used on the board.
            2.  Build the Vector instance with the params.
            3.  Send an exception chain in the ValidationResult if
                    * The vector requires insertion into the board but the insertion fails.
            4.  Return the Vector instance in the ValidationResult.
        Args:
            blueprint: VectorBlueprint
            toolkit: VectorToolkit
        Returns:
            ValidationResult[VectorBlueprint]
        Raises:
            VectorBuildException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        if toolkit is None:
            toolkit = MathToolkit()
        
        # Handle the case that, either component is out of bounds.
        for num in [blueprint.x, blueprint.y]:
            validation_result = toolkit.number_validator.validate(
                floor=0,
                ceiling=BoardDimensionSetting.entry[BoardProperty.KNIGHT_RADIUS],
                candidate=abs(num)
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    VectorAssemblyPrimingException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=VectorAssemblyPrimingException.MSG,
                        err_code=VectorAssemblyPrimingException.ERR_CODE,
                        ex=validation_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(blueprint)
    
# Register the operation.
WorkerRegistryController.register_worker(worker=VectorAssemblyPrimer)
