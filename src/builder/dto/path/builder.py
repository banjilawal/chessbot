# src/builder/dto/path/builder.py

"""
Module: builder.dto.path.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import CircularPathException, TokenPathDtoBuilderException
from model import Square, Token, TokenPathDTO
from result import BuildResult, MethodResultType
from toolkit import TokenPathToolkit
from util import LoggingLevelRouter


class TokenPathDtoBuilder:
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner
    
    Responsibilities:
        1.  Ensure a new TokenPathDto instance is born safe and reliable.
    
    Attributes:
    
    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> BuildResult[Token]
    
    Super Class:
        Builder
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            token: Token,
            destination: Square,
            toolkit: TokenPathToolkit | None = None,
    ) -> BuildResult[TokenPathDTO]:
        """
        Action:
            1.  Return a failure result containing an exception chain if either:
                    -   The collision_detector
                    -   The rank_quota_analyzer
                do not complete their work.
            2.  Otherwise, send a deletion denial if
                    -   The TokenStack is full.
                    -   The item collides with an existing stack member.
                    -   The quota for the token's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            token: Token
            destination: Square
            toolkit: TokenPathToolkit
        Returns:
            BuildResult
        Raises:
            TokenDeleteBuilderException
            TokenStackFullException
        """
        method =  f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TokenPathToolkit()
            
        origin_search_result = toolkit.origin_searcher.run(
            token=token,
            readiness_analyzer=toolkit.readiness_analyzer
        )
        # Handle the case that, the origin_searcher is not successful.
        if origin_search_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                TokenPathDtoBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPathDtoBuilderException.MSG,
                    err_code=TokenPathDtoBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=origin_search_result.exception,
                )
            )
        origin = origin_search_result.payload[0]
        
        # Handle the case that, the token is already at the destination.
        token_destination_validation_result = toolkit.destination_validator.run(
            token=token,
            destination=destination,
            token_validator=toolkit.token_validator,
            square_validator=toolkit.square_validator,
            relation_analyzer=toolkit.relation_analyzer,
        )
        if token_destination_validation_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                TokenPathDtoBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPathDtoBuilderException.MSG,
                    err_code=TokenPathDtoBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=token_destination_validation_result.exception,
                )
            )
        # Handle the case that, the origin and destination are the same.
        if origin == destination:
            # Return the exception chain on failure
            return BuildResult.failure(
                TokenPathDtoBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPathDtoBuilderException.MSG,
                    err_code=TokenPathDtoBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=CircularPathException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=CircularPathException.MSG,
                        err_code=CircularPathException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(
            payload=TokenPathDTO(
                token=token,
                origin=origin,
                destination=destination,
            )
        )

    