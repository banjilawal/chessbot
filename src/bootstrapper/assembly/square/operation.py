# src/bootstrapper/assembly/square/operation.py

"""
Module: bootstrapper.assembly.square.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from controller import WorkerRegistryController
from err import PrimingSquareAssemblyException
from model import Square, SquareBlueprint
from operation import AssemblyPrimer
from report import CollisionReport
from result import AnalysisResult, ValidationResult
from toolkit import SquareToolkit
from util import LoggingLevelRouter


class SquareAssemblyPrimer(AssemblyPrimer[Square]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner
    
    Responsibilities:
        1.  Ensure a new Square instance is born safe and reliable.
    
    Attributes:
    
    Provides:
        -   def execute(
                    blueprint: SquareBlueprint,
                    toolkit: SquareToolkit,
            ) -> ValidationResult[SquareBlueprint]
    
    Super Class:
        AssemblyPrimer
    """
    NAME = "square_assembly_primer"
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def execute(
            cls,
            blueprint: SquareBlueprint,
            toolkit: SquareToolkit,
    ) -> ValidationResult[SquareBlueprint]:
        """
        Action:
            1.  Send an exception chain in the BuildResult if
                    -   Any build param fails does not pass a validation check.
                    -   The square's attributes have already been used on the board.
            4.  Otherwise, send the success result.
        Args:
            blueprint: SquareBlueprint
            toolkit: SquareToolkit
        Returns:
            ValidationResult[SquareBlueprint]
        Raises:
            PrimingSquareAssemblyException
        """
        method = f"{cls.__class__.__name__}.build"
        
        if toolkit is None:
            toolkit = SquareToolkit()
            
        # Handle the case that, a assembly param does not pass a validation check.
        blueprint_validation_result = cls._run_validations(
            blueprint=blueprint,
            toolkit=toolkit,
        )
        if blueprint_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingSquareAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingSquareAssemblyException.MSG,
                    err_code=PrimingSquareAssemblyException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        # Handle the case that, a blueprint value has already been used.
        collision_analysis_result = cls._run_collision_analysis(
            blueprint=blueprint
        )
        if collision_analysis_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingSquareAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingSquareAssemblyException.MSG,
                    err_code=PrimingSquareAssemblyException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        return ValidationResult.success(
            SquareBlueprint(
                id=blueprint_validation_result.payload.id,
                name=blueprint_validation_result.payload.name,
                coord=blueprint_validation_result.payload.coord,
                board=blueprint_validation_result.payload.board,
                formation=blueprint_validation_result.payload.formation,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_validations(cls,
            blueprint: SquareBlueprint,
            toolkit: SquareToolkit,
    ) -> ValidationResult[SquareBlueprint]:
        """
        """
        method = f"{cls.__name__}._run_validations"
        
        # Handle the case that, the id is not certified as safe.
        id_validation_result = toolkit.identity_service.verify_priming_id(
            id=blueprint.id,
            class_name="Square",
        )
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingSquareAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingSquareAssemblyException.MSG,
                    err_code=PrimingSquareAssemblyException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the name does not pass a validation check.
        name_validation_result = toolkit.identity_service.validate_name(
            candidate=blueprint.name
        )
        if name_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingSquareAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingSquareAssemblyException.MSG,
                    err_code=PrimingSquareAssemblyException.ERR_CODE,
                    ex=name_validation_result.exception,
                )
            )
        # Handle the case that, the coord does not pass a validation check.
        coord_validation_result = toolkit.coord_validator.execute(
            candidate=blueprint.coord
        )
        if coord_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingSquareAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingSquareAssemblyException.MSG,
                    err_code=PrimingSquareAssemblyException.ERR_CODE,
                    ex=coord_validation_result.exception,
                )
            )
        # Handle the case that, the coord does not pass a validation check.
        if blueprint.formation is not None:
            formation_validation_result = toolkit.formation_service.validator.execute(
                candidate=blueprint.formation
            )
            if formation_validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PrimingSquareAssemblyException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=PrimingSquareAssemblyException.MSG,
                        err_code=PrimingSquareAssemblyException.ERR_CODE,
                        ex=formation_validation_result.exception,
                    )
                )
        # Handle the case that, the board is flagged unsafe.
        board_validator_result = toolkit.board_validator.execute(
            candidate=blueprint.board
        )
        if board_validator_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingSquareAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingSquareAssemblyException.MSG,
                    err_code=PrimingSquareAssemblyException.ERR_CODE,
                    ex=board_validator_result.exception,
                )
            )
        # --- Return the work product. ---#
        return ValidationResult.success(
            SquareBlueprint(
                name=blueprint.name,
                coord=blueprint.coord,
                board=blueprint.board,
                formation=blueprint.formation,
                id=id_validation_result.payload,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_collision_analysis(cls, blueprint: SquareBlueprint, ) -> AnalysisResult[CollisionReport]:
        """
        Verify none of the blueprint values have already been used.

        Action:
            1.  Send an exception chain in the AnalysisResult if any following occurs:
                    -   The analysis is not completed.
                    -   A collision occurred.
            2.  Otherwise, forward the success result.
        Args:
            blueprint: SquareBlueprint
        Returns:
            ValidationResult[Blueprint]
        Raises:
            PrimingSquareAssemblyException
        """
        method = f"{cls.__name__}._run_collision_analysis"
        
        # Handle the case that a blueprint value has already been used.
        collision_analysis_result = blueprint.board.squares.run_collision_analysis(
            blueprint=blueprint
        )
        if collision_analysis_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                PrimingSquareAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingSquareAssemblyException.MSG,
                    err_code=PrimingSquareAssemblyException.ERR_CODE,
                    ex=collision_analysis_result.exception,
                )
            )
        if collision_analysis_result.payload.collision_exists:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingSquareAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingSquareAssemblyException.MSG,
                    err_code=PrimingSquareAssemblyException.ERR_CODE,
                    ex=collision_analysis_result.payload.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return collision_analysis_result


# Register the operation.
WorkerRegistryController.register_worker(worker=SquareAssemblyPrimer)
