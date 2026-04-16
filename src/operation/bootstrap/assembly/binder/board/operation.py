# src/model/binder/assembly/exception.py

"""
Module: model.binder.assembly.assembly
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from microservice import IdentityService, TeamBinderService
from model import Board, TeamBinderBinderBlueprint, BoardTeamBinderBlueprint
from model.catalog import SchemaService
from operation import AssemblyBootstrapper
from result import ValidationResult
from system import AssemblyResult, Assembly, LoggingLevelRouter
from model.teamBinder import (
    BlackTeamBinderHasWrongSchemaException, TeamBinder, TeamBinderBinder, TeamBinderBinderAssemblyException,
    TeamBinderSchemaCollisionException, TeamBinderValidator, WhiteTeamBinderHasWrongSchemaException
)
from toolkit import TeamBinderBinderToolkit, TeamBinderToolkit


class TeamBinderBinderAssemblyBootstrapper(AssemblyBootstrapper[TeamBinderBinder]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            blueprint: TeamBinderBinderBlueprint,
            toolkit: TeamBinderBinderToolkit | None = None,
    ) -> ValidationResult[TeamBinderBinder]:
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the toolkit flags a blueprint component unsafe.
        blueprint_validation_result = cls._run_validations(
            blueprint=blueprint,
            toolkit=toolkit,
        )
        if blueprint_validation_result.is_failure:
            # Return the exception chain on failure.
            return AssemblyResult.failure(
                TeamBinderBinderAssemblyException(
                    msg=f"{method}: {TeamBinderBinderAssemblyException.MSG}",
                    ex=WhiteTeamBinderHasWrongSchemaException(
                        f"{method}: {WhiteTeamBinderHasWrongSchemaException.MSG}",
                    )
                )
            )
        return ValidationResult.success(
            BoardTeamBinderBlueprint(
                id=blueprint_validation_result.payload.id,
                board=blueprint_validation_result.payload.board,
                schema=blueprint_validation_result.payload.schema,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_validations(cls,
            blueprint: BoardTeamBinderBlueprint,
            toolkit: TeamBinderToolkit,
    ) -> ValidationResult[BoardTeamBinderBlueprint]:
        """
        """
        method = f"{cls.__name__}._run_validations"
        
        # Handle the case that, the id is not certified as safe.
        id_validation_result = toolkit.identity_service.verify_bootstrap_id(
            id=blueprint.id,
            class_name="TeamBinder",
        )
        if id_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTeamBinderAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTeamBinderAssemblyException.MSG,
                    err_code=BootstrapTeamBinderAssemblyException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the schema does not pass a validation check.
        schema_validation_result = toolkit.schema_service.validator.validate(
            candidate=blueprint.schema
        )
        if schema_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTeamBinderAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTeamBinderAssemblyException.MSG,
                    err_code=BootstrapTeamBinderAssemblyException.ERR_CODE,
                    ex=schema_validation_result.exception,
                )
            )
        # Handle the case that, the board does not pass a validation check.
        board_validation_result = toolkit.board_service.validator.validate(blueprint.board)
        if board_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTeamBinderAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTeamBinderAssemblyException.MSG,
                    err_code=BootstrapTeamBinderAssemblyException.ERR_CODE,
                    ex=board_validation_result.exception,
                )
            )
        return ValidationResult.success(
            BoardTeamBinderBlueprint(
                id=id_validation_result.payload,
                schema=blueprint.schema,
                board=blueprint.board,
            )
        )
