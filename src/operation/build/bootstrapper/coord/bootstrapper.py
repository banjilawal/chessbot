# src/operation/bootstrapper/token/bootstrapper.py

"""
Module: operation.bootstrapper.token.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import TokenBootstrapBuildException
from model import SquareContext, Token, TokenBlueprint
from operation import BuildBootstrapper

from result import BuildResult, BuildResult
from search import SquareNotFoundException
from system import IdFactory, LoggingLevelRouter
from toolkit import TokenToolkit


class TokenBuildBootstrapper(BuildBootstrapper[Token]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            blueprint: TokenBlueprint,
            toolkit: TokenToolkit | None = None
    ) -> BuildResult[TokenBlueprint]:
        method = f"{cls.__name__}.execute"
        
        if toolkit is None:
            toolkit = TokenToolkit()
            
        # Handle the case that, the id is not certified as safe.
        id_validation_result = cls._verify_id(blueprint=blueprint, toolkit=toolkit)
        if id_validation_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBootstrapBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBootstrapBuildException.MSG,
                    err_code=TokenBootstrapBuildException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the team does not pass a validation check.
        team_validation = toolkit.team_service.validator.validate(blueprint.team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBootstrapBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBootstrapBuildException.MSG,
                    err_code=TokenBootstrapBuildException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that, the formation does not pass a validation check.
        formation_validation = toolkit.formation_service.validator.validate(blueprint.formation)
        if formation_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBootstrapBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBootstrapBuildException.MSG,
                    err_code=TokenBootstrapBuildException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        square_search_result = blueprint.team.roster.search(
            context=SquareContext(formation=blueprint.formation)
        )
        if square_search_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBootstrapBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBootstrapBuildException.MSG,
                    err_code=TokenBootstrapBuildException.ERR_CODE,
                    ex=square_search_result.exception,
                )
            )
        if square_search_result.is_empty:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBootstrapBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBootstrapBuildException.MSG,
                    err_code=TokenBootstrapBuildException.ERR_CODE,
                    ex=SquareNotFoundException(
                        msg=SquareNotFoundException.MSG,
                        err_code=SquareNotFoundException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that its Rank instance request is not satisfied.
        rank_build_result = toolkit.rank_service.builder.build(persona=blueprint.formation.persona)
        if rank_build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBootstrapBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBootstrapBuildException.MSG,
                    err_code=TokenBootstrapBuildException.ERR_CODE,
                    ex=rank_build_result.exception,
                )
            )
        id_verification_result = cls._verify_id(blueprint=blueprint, toolkit=toolkit)
        if id_verification_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBootstrapBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBootstrapBuildException.MSG,
                    err_code=TokenBootstrapBuildException.ERR_CODE,
                    ex=rank_build_result.exception,
                )
            )
        collision_analysis_result = blueprint.team.roster.run_collision_analysis(blueprint=blueprint)
        if not collision_analysis_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBootstrapBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBootstrapBuildException.MSG,
                    err_code=TokenBootstrapBuildException.ERR_CODE,
                    ex=rank_build_result.exception,
                )
            )
        if collision_analysis_result.payload.collision_exists:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBootstrapBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBootstrapBuildException.MSG,
                    err_code=TokenBootstrapBuildException.ERR_CODE,
                    ex=collision_analysis_result.payload.exception,
                )
            )
        return BuildResult.success(
            TokenBlueprint(
                team=blueprint.team,
                formation=blueprint.formation,
                rank=rank_build_result.payload.rank,
                opening_square=square_search_result.payload[0],
                id=id_verification_result.payload,
            )
        )

    @classmethod
    def _verify_id(
            cls,
            blueprint: TokenBlueprint,
            toolkit: TokenToolkit
    ) -> BuildResult[int]:
        method = f"{cls.__name__}._verify_id"
        
        if blueprint.id is None:
            return BuildResult.success(IdFactory.next_id(class_name="Token"))
        
        id_validation = toolkit.identity_service.validate_id(blueprint.id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBootstrapBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBootstrapBuildException.MSG,
                    err_code=TokenBootstrapBuildException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )