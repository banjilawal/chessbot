# src/model/binder/assembly/exception.py

"""
Module: model.binder.assembly.assembly
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from microservice import IdentityService, BoardTeamBinderService
from model import Board, TeamBinderBinderBlueprint, BoardBinderBlueprint
from model.catalog import SchemaService
from operation import AssemblyPrimer
from result import ValidationResult
from system import AssemblyResult, Assembly, LoggingLevelRouter
from model.teamBinder import (
    BlackTeamBinderHasWrongSchemaException, TeamBinder, TeamBinderBinder, TeamBinderBinderAssemblyException,
    TeamBinderSchemaCollisionException, TeamBinderValidator, WhiteTeamBinderHasWrongSchemaException
)
from toolkit import TeamBinderBinderToolkit, TeamBinderToolkit


class TeamBinderBinderAssemblyPrimer(AssemblyPrimer[TeamBinderBinder]):
    
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
            # Send the exception chain on failure.
            return AssemblyResult.failure(
                TeamBinderBinderAssemblyException(
                    msg=f"{method}: {TeamBinderBinderAssemblyException.MSG}",
                    ex=WhiteTeamBinderHasWrongSchemaException(
                        f"{method}: {WhiteTeamBinderHasWrongSchemaException.MSG}",
                    )
                )
            )
        return ValidationResult.success(
            BoardBinderBlueprint(
                id=blueprint_validation_result.payload.id,
                board=blueprint_validation_result.payload.board,
                schema=blueprint_validation_result.payload.schema,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_validations(cls,
            blueprint: BoardBinderBlueprint,
            toolkit: TeamBinderToolkit,
    ) -> ValidationResult[BoardBinderBlueprint]:
        """
        """
        method = f"{cls.__name__}._run_validations"
        
        # Handle the case that, the id is not certified as safe.
        id_validation_result = toolkit.identity_service.verify_priming_id(
            id=blueprint.id,
            class_name="TeamBinder",
        )
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingTeamBinderAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingTeamBinderAssemblyException.MSG,
                    err_code=PrimingTeamBinderAssemblyException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the schema does not pass a validation check.
        schema_validation_result = toolkit.schema_service.execute.build(
            candidate=blueprint.schema
        )
        if schema_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingTeamBinderAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingTeamBinderAssemblyException.MSG,
                    err_code=PrimingTeamBinderAssemblyException.ERR_CODE,
                    ex=schema_validation_result.exception,
                )
            )
        # Handle the case that, the board does not pass a validation check.
        board_validation_result = toolkit.board_service.execute.build(blueprint.board)
        if board_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingTeamBinderAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingTeamBinderAssemblyException.MSG,
                    err_code=PrimingTeamBinderAssemblyException.ERR_CODE,
                    ex=board_validation_result.exception,
                )
            )
        return ValidationResult.success(
            BoardBinderBlueprint(
                id=id_validation_result.payload,
                schema=blueprint.schema,
                board=blueprint.board,
            )
        )
