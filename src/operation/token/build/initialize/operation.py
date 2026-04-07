# src/integrity/build/token/builder.py

"""
Module: integrity.build.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict

from catalog import Formation, Persona
from err import TokenBuildInitializationException
from integrity import Builder
from microservice import RankService
from model import CombatantToken, KingToken, PawnToken, Team, Token
from result import BuildResult, BuildResult
from system import IdFactory, LoggingLevelRouter
from toolkit.integrity.token.toolkit import TokenIntegrityToolkit


class TokenBuildInitializer:

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            owner: Team,
            formation: Formation,
            id: int = None,
            toolkit: TokenIntegrityToolkit = None,
    ) -> BuildResult[Dict[str, Any]]:
        """
        Build a safe Token.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following
                occur:
                    -   Either id, schema, team. formation fail a validation check.
                    -   The token belongs on a different team.
                    -   The team has already filled the position.
                    -   The token's rank cannot be built.
                    -   The token cannot register with its team.
            2.  Otherwise, build the token then, send the success result.
        Args:
            id: int
            owner: Team
            formation: Formation
            toolkit: TokenIntegrityToolkit
        Returns:
            BuildResult[Token]
        Raises:
            TokenBuildInitializationException
        """
        method = f"{cls.__name__}.execute"
        
        if id is None:
            id = IdFactory.next_id(class_name="Token")
        if toolkit is None:
            toolkit = TokenIntegrityToolkit()
        
        # Handle the case that, the id does not pass a validation check.
        id_validation = toolkit.identity_service.validate_id(id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildInitializationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=TokenBuildInitializationException.OP,
                    msg=TokenBuildInitializationException.MSG,
                    err_code=TokenBuildInitializationException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that, the team does not pass a validation check.
        owner_validation = toolkit.team_service.validator.validate(owner)
        if owner_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildInitializationException(
                    cls_mthd=method,
                    cls_name=method.__name__,
                    op=TokenBuildInitializationException.OP,
                    msg=TokenBuildInitializationException.MSG,
                    err_code=TokenBuildInitializationException.ERR_CODE,
                    ex=owner_validation.exception,
                )
            )
        # Handle the case that, the formation does not pass a validation check.
        formation_validation = toolkit.formation_service.validator.validate(formation)
        if formation_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildInitializationException(
                    cls_mthd=method,
                    cls_name=method.__name__,
                    op=TokenBuildInitializationException.OP,
                    msg=TokenBuildInitializationException.MSG,
                    err_code=TokenBuildInitializationException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # Handle the case that its Rank instance request is not satisfied.
        rank_build_result = toolkit.rank_service.builder.build(persona=formation.persona)
        if rank_build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildInitializationException(
                    cls_mthd=method,
                    cls_name=method.__name__,
                    op=TokenBuildInitializationException.OP,
                    msg=TokenBuildInitializationException.MSG,
                    err_code=TokenBuildInitializationException.ERR_CODE,
                    ex=rank_build_result.exception,
                )
            )
        # ---Forward the work product. ---#
        return BuildResult.success(
            {"id":id, "owner": owner, "formation": formation, "rank": rank_build_result.payload}
        )

        