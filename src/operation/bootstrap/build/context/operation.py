# src/operation/bootstrap/context/bootstrap.py

"""
Module: operation.bootstrap.context.bootstrap
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analysis import CollisionReport
from err import BootstrapContextBuildException
from model import Context, ContextBlueprint
from operation import BuildBootstrap

from result import BuildResult, ValidationResult
from system import IdFactory, LoggingLevelRouter
from toolkit import ContextToolkit


class BootstrapContextBuild(BuildBootstrap[Context]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            blueprint: ContextBlueprint,
            toolkit: ContextToolkit = None
    ) -> ValidationResult[ContextBlueprint]:
        method = f"{cls.__name__}.execute"
        
        if toolkit is None:
            toolkit = ContextToolkit()
            
        # Handle the case that, the id is not certified as safe.
        id_validation_result = cls._verify_id(blueprint=blueprint, toolkit=toolkit)
        if id_validation_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                BootstrapContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapContextBuildException.MSG,
                    err_code=BootstrapContextBuildException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the team does not pass a validation check.
        team_validation = toolkit.team_service.validator.validate(blueprint.team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                BootstrapContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapContextBuildException.MSG,
                    err_code=BootstrapContextBuildException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that, the formation does not pass a validation check.
        formation_validation = toolkit.formation_service.validator.validate(blueprint.formation)
        if formation_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                BootstrapContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapContextBuildException.MSG,
                    err_code=BootstrapContextBuildException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # Handle the case that its Rank instance request is not satisfied.
        rank_build_result = toolkit.rank_service.builder.build(persona=blueprint.formation.persona)
        if rank_build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                BootstrapContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapContextBuildException.MSG,
                    err_code=BootstrapContextBuildException.ERR_CODE,
                    ex=rank_build_result.exception,
                )
            )
        id_verification_result = cls._verify_id(blueprint=blueprint, toolkit=toolkit)
        if id_verification_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                BootstrapContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapContextBuildException.MSG,
                    err_code=BootstrapContextBuildException.ERR_CODE,
                    ex=rank_build_result.exception,
                )
            )
        collision_analysis_result = blueprint.team.roster.run_collision_analysis(blueprint=blueprint)
        if not collision_analysis_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                BootstrapContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapContextBuildException.MSG,
                    err_code=BootstrapContextBuildException.ERR_CODE,
                    ex=rank_build_result.exception,
                )
            )
        if collision_analysis_result.payload.collision_exists:
            # Return the exception chain on failure.
            return BuildResult.failure(
                BootstrapContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapContextBuildException.MSG,
                    err_code=BootstrapContextBuildException.ERR_CODE,
                    ex=collision_analysis_result.payload.exception,
                )
            )

    @classmethod
    def _verify_id(
            cls,
            blueprint: ContextBlueprint,
            toolkit: ContextToolkit
    ) -> ValidationResult[int]:
        method = f"{cls.__name__}._verify_id"
        
        if blueprint.id is None:
            return ValidationResult.success(IdFactory.next_id(class_name="Context"))
        
        id_validation = toolkit.identity_service.validate_id(blueprint.id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                BootstrapContextBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapContextBuildException.MSG,
                    err_code=BootstrapContextBuildException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )