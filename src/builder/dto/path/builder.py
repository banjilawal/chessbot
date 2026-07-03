# src/builder/dto/path/builder.py

"""
Module: builder.dto.path.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import CircularPathException
from model import Square, Token, TokenPathDTO
from result import BuildResult, MethodResultType
from toolkit import TokenPathToolkit
from util import LoggingLevelRouter


class TokenPathDtoBuilder:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a deletion.

    Attributes:

    Provides:
        -   execute(
                    cls,
                    token: Token,
                    token_stack: TokenStackService,
                    rank_service: RankService = RankService(),
                    rank_quota_analyzer: RankQuotaAnalyzer = RankQuotaAnalyzer(),
                    collision_detector: TokenCollisionAnalyst = TokenCollisionAnalyst(),
            ) -> BuildResult

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
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
            
        origin_search_result = toolkit.origin_searcher.execute(
            token=token,
            readiness_analyzer=toolkit.readiness_analyzer
        )
        # Handle the case that, the origin_searcher is not successful.
        if origin_search_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                TokenPahDtoBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPahDtoBuilderException.MSG,
                    err_code=TokenPahDtoBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=origin_search_result.exception,
                )
            )
        origin = origin_search_result.payload[0]
        
        # Handle the case that, the token is already at the destination.
        token_destination_validation_result = toolkit.destination_validator.execute(
            token=token,
            destination=destination,
            token_validator=toolkit.token_validator,
            square_validator=toolkit.square_validator,
            relation_analyzer=toolkit.relation_analyzer,
        )
        if token_destination_validation_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                TokenPahDtoBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPahDtoBuilderException.MSG,
                    err_code=TokenPahDtoBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=token_destination_validation_result.exception,
                )
            )
        # Handle the case that, the origin and destination are the same.
        if origin == destination:
            # Return the exception chain on failure
            return BuildResult.failure(
                TokenPahDtoBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPahDtoBuilderException.MSG,
                    err_code=TokenPahDtoBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=CircularPathException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=CircularPathException.MSG,
                        err_code=CircularPathException.ERR_CODE,
                    ),
                )
            )
        return BuildResult.success(
            payload=TokenPathDTO(
                token=token,
                origin=origin,
                destination=destination,
            )
        )

    