# src/operation/bootstrapper/token/bootstrapper.py

"""
Module: operation.bootstrapper.token.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Token

from operation import Bootstrapper
from result import BuildResult, ValidationResult
from system import IdFactory, LoggingLevelRouter
from toolkit import IntegrityToolkit, TokenIntegrityToolkit


class TokenBuildBootstrapper(Bootstrapper[Token]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            blueprint: TokenBlueprint,
            toolkit: TokenIntegrityToolkit = None
    ) -> ValidationResult[TokenBlueprint]:
        method = f"{cls.__name__}.execute"
        
        if toolkit is None:
            toolkit = TokenIntegrityToolkit()
        
        # Handle the case that, the team does not pass a validation check.
        team_validation = toolkit.team_service.validator.validate(blueprint.team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildBootStrapException(
                    cls_mthd=method,
                    cls_name=method.__name__,
                    op=TokenBuildBootStrapException.OP,
                    msg=TokenBuildBootStrapException.MSG,
                    err_code=TokenBuildBootStrapException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that, the formation does not pass a validation check.
        formation_validation = toolkit.formation_service.validator.validate(blueprint.formation)
        if formation_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildBootStrapException(
                    cls_mthd=method,
                    cls_name=method.__name__,
                    op=TokenBuildBootStrapException.OP,
                    msg=TokenBuildBootStrapException.MSG,
                    err_code=TokenBuildBootStrapException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # Handle the case that its Rank instance request is not satisfied.
        rank_build_result = toolkit.rank_service.builder.build(persona=blueprint.formation.persona)
        if rank_build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildBootStrapException(
                    cls_mthd=method,
                    cls_name=method.__name__,
                    op=TokenBuildBootStrapException.OP,
                    msg=TokenBuildBootStrapException.MSG,
                    err_code=TokenBuildBootStrapException.ERR_CODE,
                    ex=rank_build_result.exception,
                )
            )
        id_verification_result = cls._verify_id(blueprint, toolkit)
        if id_verification_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildBootStrapException(
                    cls_mthd=method,
                    cls_name=method.__name__,
                    op=TokenBuildBootStrapException.OP,
                    msg=TokenBuildBootStrapException.MSG,
                    err_code=TokenBuildBootStrapException.ERR_CODE,
                    ex=rank_build_result.exception,
                )
            )
        collision_analysis_result = blueprint.team.roster.run_collision_analysis(blueprint=blueprint)
        if not collision_analysis_result.s
        return ValidationResult.success(
            TokenBlueprint(
                team=blueprint.team,
                formation=blueprint.formation,
                rank=rank_build_result.payload,
                id=id_verification_result.payload,
            )
        )
    
        
    @classmethod
    def _verify_id(cls, blueprint: TokenBlueprint, toolkit: IntegrityToolkit) -> ValidationResult[int]:
        
        if blueprint.id is None:
            return ValidationResult.success(IdFactory.next_id(class_name="Token"))
        
        id_validation = toolkit.identity_service.validate_id(blueprint.id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildBootStrapException(
                    cls_mthd=method,
                    cls_name=method.__name__,
                    op=TokenBuildBootStrapException.OP,
                    msg=TokenBuildBootStrapException.MSG,
                    err_code=TokenBuildBootStrapException.ERR_CODE,
                    ex=rank_build_result.exception,
                )
            )