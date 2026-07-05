# src/operation/assembly/scalar/operation.py

"""
Module: operation.assembly.scalar.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from result import BuildResult
from operation import Assembler
from toolkit import ScalarToolkit
from util import LoggingLevelRouter
from err import ScalarAssemblyException
from model import Scalar, ScalarBlueprint
from controller import WorkerRegistryController


class ScalarAssembler(Assembler[Scalar]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Scalar instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    blueprint: ScalarBlueprint,
                    toolkit: ScalarToolkit,
            ) -> ValidationResult[ScalarBlueprint]

     Super Class:
        Assembler
     """
    NAME = "scalar_assembler"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            blueprint: ScalarBlueprint,
            toolkit: ScalarToolkit | None = None,
    ) -> BuildResult[Scalar]:
        """
        Action:
            1.  Send an exception chain in the BuildResult if
                    -   Any build param fails does not pass a validation check.
            4.  Otherwise, send the success result.
        Args:
            blueprint: ScalarBlueprint
            toolkit: ScalarToolkit
        Returns:
            BuildResult[Scalar] 
        Raises:
            ScalarAssemblyException
        """
        method = f"{cls.__name__}.validate"
        
        if toolkit is None:
            toolkit = ScalarToolkit()
        
        # Handle the case that, the validator is not primed.
        validation_result = toolkit.number_validator.build(
            candidate=blueprint.magnitude,
        )
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ScalarAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ScalarAssemblyException.MSG,
                    err_code=ScalarAssemblyException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(Scalar(magnitude=blueprint.magnitude))

# Register the operation.
WorkerRegistryController.register_worker(worker=ScalarAssembler)
