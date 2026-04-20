# src/integrity/build/vector/builder.py

"""
Module: integrity.build.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import BootstrapVectorAssemblyException
from model import Board, Vector, VectorBlueprint
from operation import AssemblyBootstrapper
from report import CollisionReport
from result import AnalysisResult, ValidationResult
from system import LoggingLevelRouter
from toolkit import VectorToolkit


class VectorAssemblyBootstrapper(AssemblyBootstrapper[Vector]):
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
                    owner: Vector,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    vector_validator: VectorValidator,
            ) -> BuildResult[Vector]

     Super Class:
         Builder
     """
    @classmethod
    @LoggingLevelRouter.monitor()
    def execute(
            cls,
            blueprint: VectorBlueprint,
            toolkit: VectorToolkit,
    ) -> ValidationResult[VectorBlueprint]:
        """
        Action:
            1.  Send an exception chain in the BuildResult if
                    -   Any build param fails does not pass a validation check.
                    -   The vector's attributes have already been used on the board.
            2.  Build the Vector instance with the params.
            3.  Send an exception chain in the BuildResult if
                    * The vector requires insertion into the board but the insertion fails.
            4.  Return the Vector instance in the BuildResult.
        Args:
            id: int
            name: str
            coord: Coord
            board: Board
            tool: VectorTool
        Returns:
            BuildResult[Vector]
            
        Raises:
            VectorBuildException
        """
        method = f"{cls.__class__.__name__}.build"
        
        if toolkit is None:
            toolkit = VectorToolkit()
            
        # Handle the case that, a assembly param does not pass a validation check.
        blueprint_validation_result = cls._run_validations(
            blueprint=blueprint,
            toolkit=toolkit,
        )
        if blueprint_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapVectorAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapVectorAssemblyException.MSG,
                    err_code=BootstrapVectorAssemblyException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        # Handle the case that, a blueprint value has already been used.
        collision_analysis_result = cls._run_collision_analysis(
            blueprint=blueprint
        )
        if collision_analysis_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapVectorAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapVectorAssemblyException.MSG,
                    err_code=BootstrapVectorAssemblyException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        return ValidationResult.success(
            VectorBlueprint(
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
            blueprint: VectorBlueprint,
            toolkit: VectorToolkit,
    ) -> ValidationResult[VectorBlueprint]:
        """
        """
        method = f"{cls.__name__}._run_validations"
        
        # Handle the case that, the id is not certified as safe.
        id_validation_result = toolkit.identity_service.verify_bootstrap_id(
            id=blueprint.id,
            class_name="Vector",
        )
        if id_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapVectorAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapVectorAssemblyException.MSG,
                    err_code=BootstrapVectorAssemblyException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the name does not pass a validation check.
        name_validation_result = toolkit.identity_service.validate_name(
            candidate=blueprint.name
        )
        if name_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapVectorAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapVectorAssemblyException.MSG,
                    err_code=BootstrapVectorAssemblyException.ERR_CODE,
                    ex=name_validation_result.exception,
                )
            )
        # Handle the case that, the coord does not pass a validation check.
        coord_validation_result = toolkit.coord_validator.validate(
            candidate=blueprint.coord
        )
        if coord_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapVectorAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapVectorAssemblyException.MSG,
                    err_code=BootstrapVectorAssemblyException.ERR_CODE,
                    ex=coord_validation_result.exception,
                )
            )
        # Handle the case that, the coord does not pass a validation check.
        if blueprint.formation is not None:
            formation_validation_result = toolkit.formation_service.validator.validate(
                candidate=blueprint.formation
            )
            if formation_validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    BootstrapVectorAssemblyException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=BootstrapVectorAssemblyException.MSG,
                        err_code=BootstrapVectorAssemblyException.ERR_CODE,
                        ex=formation_validation_result.exception,
                    )
                )
        # Handle the case that, the board is flagged unsafe.
        board_validation_result = toolkit.board_validator.validate(
            candidate=blueprint.board
        )
        if board_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapVectorAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapVectorAssemblyException.MSG,
                    err_code=BootstrapVectorAssemblyException.ERR_CODE,
                    ex=board_validation_result.exception,
                )
            )
        # --- Return the work product. ---#
        return ValidationResult.success(
            VectorBlueprint(
                name=blueprint.name,
                coord=blueprint.coord,
                board=blueprint.board,
                formation=blueprint.formation,
                id=id_validation_result.payload,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_collision_analysis(cls, blueprint: VectorBlueprint, ) -> AnalysisResult[CollisionReport]:
        """
        Verify none of the blueprint values have already been used.

        Action:
            1.  Send an exception chain in the AnalysisResult if any following occurs:
                    -   The analysis is not completed.
                    -   A collision occurred.
            2.  Otherwise, forward the success result.
        Args:
            blueprint: VectorBlueprint
        Returns:
            ValidationResult[Blueprint]
        Raises:
            BootstrapVectorAssemblyException
        """
        method = f"{cls.__name__}._run_collision_analysis"
        
        # Handle the case that a blueprint value has already been used.
        collision_analysis_result = blueprint.board.vectors.run_collision_analysis(
            blueprint=blueprint
        )
        if collision_analysis_result.is_failure:
            # Return the exception chain on failure.
            return AnalysisResult.failure(
                BootstrapVectorAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapVectorAssemblyException.MSG,
                    err_code=BootstrapVectorAssemblyException.ERR_CODE,
                    ex=collision_analysis_result.exception,
                )
            )
        if collision_analysis_result.payload.collision_exists:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapVectorAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapVectorAssemblyException.MSG,
                    err_code=BootstrapVectorAssemblyException.ERR_CODE,
                    ex=collision_analysis_result.payload.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return collision_analysis_result
