# src/carrier_validator/assembly/coord/operation.py

"""
Module: carrier_validator.assembly.coord.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from setting import BoardDimensionSetting, BoardProperty
from controller import WorkerRegistryController
from err import PrimingCoordAssemblyException
from toolkit import CoordToolkit
from result import ValidationResult
from model import Coord, CoordBlueprint
from operation import AssemblyPrimer
from util import LoggingLevelRouter


class CoordAssemblyPrimer(AssemblyPrimer[Coord]):
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
                    toolkit: CoordToolkit,
            ) -> ValidationResult[CoordBlueprint]:
    
    Super Class:
        AssemblyPrimer
    """
    NAME = "coord_assembly_primer"
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def execute(
            cls,
            blueprint: CoordBlueprint,
            toolkit: CoordToolkit | None = None,
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
            CoordBuilderException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        if toolkit is None:
            toolkit = CoordToolkit()
        
        # Handle the case that, either component is out of bounds.
        for component in [blueprint.x, blueprint.y]:
            validation_result = toolkit.number_validator.execute(
                floor=0,
                ceiling=BoardDimensionSetting.entry[BoardProperty.MAX_COLUMN_INDEX],
                candidate=abs(component)
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PrimingCoordAssemblyException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PrimingCoordAssemblyException.MSG,
                        err_code=PrimingCoordAssemblyException.ERR_CODE,
                        ex=validation_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(blueprint)

# Register the operation.
WorkerRegistryController.register_worker(worker=CoordAssemblyPrimer)
