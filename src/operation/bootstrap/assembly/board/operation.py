# src/operation/bootstrap/assembly/board/operation.py

"""
Module: operation.bootstrap.assembly.board.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from controller import WorkerRegistryController
from toolkit import BoardToolkit
from result import ValidationResult
from model import Board, BoardBlueprint
from operation import AssemblyBootstrapper
from err import BootstrapBoardAssemblyException
from util import LoggingLevelRouter


class BoardAssemblyBootstrapper(AssemblyBootstrapper[Board]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Assembly Process Owner
    
    Responsibilities:
        1.  Ensure a new Board instance is born safe and reliable.
    
    Attributes:
    
    Provides:
        -   def execute(
                blueprint: BoardBlueprint,
                toolkit: BoardToolkit,
        ) -> ValidationResult[BoardBlueprint]:
    
    Super Class:
        AssemblyBootstrapper
    """
    NAME = "board_assembly_bootstrapper"
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def execute(
            cls,
            blueprint: BoardBlueprint,
            toolkit: BoardToolkit | None = None,
    ) -> ValidationResult[BoardBlueprint]:
        """
        Verify the integrity of the blueprint.
        
        Action:
            1.  Send an exception in the ValidationResult if any of these conditions occur:
                    -   Any component in the blueprint is flagged.
        Attributes:
            blueprint: BoardBlueprint
            toolkit: BoardToolkit
        Returns:
            ValidationResult[Board]
        Raises:
            BootstrapBoardAssemblyException
        """
        method = f"{cls.__name__}.execute"
        
        if toolkit is None:
            toolkit = BoardToolkit()
        
        # Handle the case that, a assembly param does not pass a validation check.
        blueprint_validation_result = cls._run_validations(
            blueprint=blueprint,
            toolkit=toolkit,
        )
        if blueprint_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BootstrapBoardAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapBoardAssemblyException.MSG,
                    err_code=BootstrapBoardAssemblyException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        return ValidationResult.success(blueprint_validation_result.payload)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_validations(cls,
            blueprint: BoardBlueprint,
            toolkit: BoardToolkit,
    ) -> ValidationResult[BoardBlueprint]:
        """
        """
        method = f"{cls.__name__}._run_validations"
        
        # Handle the case that, the id is not certified as safe.
        id_validation_result = toolkit.identity_service.verify_bootstrap_id(
            id=blueprint.id,
            class_name="Board",
        )
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BootstrapBoardAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapBoardAssemblyException.MSG,
                    err_code=BootstrapBoardAssemblyException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the arena does not pass a validation check.
        arena_validator_result = toolkit.arena_validator.validate(
            candidate=blueprint.arena
        )
        if arena_validator_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BootstrapBoardAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapBoardAssemblyException.MSG,
                    err_code=BootstrapBoardAssemblyException.ERR_CODE,
                    ex=arena_validator_result.exception,
                )
            )
        return ValidationResult.success(
            BoardBlueprint(
                id=id_validation_result.payload,
                arena=blueprint.arena,
            )
        )


# Register the operation.
WorkerRegistryController.register(worker=BoardAssemblyBootstrapper)

        