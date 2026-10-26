# src/transit/dispatcher/fabrication/search/stack/home/dispatcher.py

"""
Module: transit.dispatcher.fabrication.search.stack.home.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from domain.context.context import TokenHomeContext
from artifcat import BuildResult
from operation.toolkit import TokenHomeContextToolkit
from util import LoggingLevelRouter
from transit.dispatcher.fabrication import StackContextBuilder


class TokenHomeContextBuilder(StackContextBuilder[TokenHomeContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a HomeContext instance is certified safe, reliable, and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    builder: HomeToolkit,
            ) -> BuildResult[Home]:

    Super Class:
        ContextBuilder
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            builder: TokenHomeContextToolkit | None = None,
    ) -> BuildResult:
        """
        Certify a candidate is a HomeContext that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if any of the following
                occur
                    - The Build is not primed.
                    - The enabled attribute fails a safety check.
                    - There is no build path for the attribute.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
            builder: HomeToolkit,
        Returns:
            BuildResult[Home]
        Raises:
            HomeContextBuilderException
            HomeContextBuildRouteException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TokenHomeContextToolkit
        
        # Handle the case that the builder is not primed.
        priming_result = toolkit.priming_builder.execute(
            job=candidate,
            target_model=candidate,
            context_null_exception=HomeContext,
            priming_builder=HomeContextNullException()
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                HomeContextBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=HomeContextBuilderException.MSG,
                    err_code=HomeContextBuilderException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into HomeContext for routing attribute testing ---#
        context = cast(TokenHomeContext, priming.payload)
        
        # Build for the search-by-id target.
        if context.id is not None:
            build_result = toolkit.identity_service.validate_id(
                candidate=context.id
            )
            if build_result.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    HomeContextBuilderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeContextBuilderException.MSG,
                        err_code=HomeContextBuilderException.ERR_CODE,
                        ex=build_result.exception
                    )
                )
            # On build success forward the work product to the caller.
            return BuildResult.success(context)
        
        # Build for the search-by-designation target.
        if context.designation is not None:
            build_result = toolkit.identity_service.validate_name(
                candidate=context.designation
            )
            if build_result.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    HomeContextBuilderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeContextBuilderException.MSG,
                        err_code=HomeContextBuilderException.ERR_CODE,
                        ex=build_result.exception
                    )
                )
                # On build success forward the work product to the caller.
            return BuildResult.success(context)
        
        # Build for the search-by-home_square target.
        if context.home_square is not None:
            build_result = toolkit.square_builder.execute(
                job=context.home_square
            )
            if build_result.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    HomeContextBuilderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeContextBuilderException.MSG,
                        err_code=HomeContextBuilderException.ERR_CODE,
                        ex=build_result.exception
                    )
                )
                # On build success forward the work product to the caller.
            return BuildResult.success(context)
        
        # Build for the search-by-coord target.
        if context.position is not None:
            build_result = toolkit.coord_builder.execute(
                job=context.position
            )
            if build_result.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    HomeContextBuilderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeContextBuilderException.MSG,
                        err_code=HomeContextBuilderException.ERR_CODE,
                        ex=build_result.exception
                    )
                )
                # On build success forward the work product to the caller.
            return BuildResult.success(context)
    
        # Build for the search-by-team target.
        if context.victim is not None:
            build_result = toolkit.team_builder.execute(
                job=context.position
            )
            if build_result.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    HomeContextBuilderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeContextBuilderException.MSG,
                        err_code=HomeContextBuilderException.ERR_CODE,
                        ex=build_result.exception
                    )
                )
                # On build success forward the work product to the caller.
            return BuildResult.success(context)
        
        # Build for the search-by-rank target.
        if context.rank is not None:
            build_result = toolkit.rank_service.builder.execute(
                job=context.rank
            )
            if build_result.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    HomeContextBuilderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeContextBuilderException.MSG,
                        err_code=HomeContextBuilderException.ERR_CODE,
                        ex=build_result.exception
                    )
                )
                # On build success forward the work product to the caller.
            return BuildResult.success(context)
        
        # Build for the search-by-color target.
        if context.team_color is not None:
            build_result = toolkit.priming_builder.execute(
                job=context.team_color,
                model_type=GameColor,
                null_exception=GameColorNullException()
            )
            if build_result.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    HomeContextBuilderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeContextBuilderException.MSG,
                        err_code=HomeContextBuilderException.ERR_CODE,
                        ex=build_result.exception
                    )
                )
                # On build success forward the work product to the caller.
            return BuildResult.success(context)
        
        # Build for the search-by-ransom target.
        if context.ransom is not None:
            build_result = toolkit.number_builder.execute(
                job=context.ransom,
                floor=Persona.KING.ransom,
                ceiling=Persona.QUEEN.ransom,
            )
            if build_result.is_failure:
                # Send the exception chain on failure.
                return BuildResult.failure(
                    HomeContextBuilderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=HomeContextBuilderException.MSG,
                        err_code=HomeContextBuilderException.ERR_CODE,
                        ex=build_result.exception
                    )
                )
                # On build success forward the work product to the caller.
            return BuildResult.success(context)
        
        # Handle the case that there is no build logic for the attribute.
        return BuildResult.failure(
            HomeContextBuilderException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=HomeContextBuilderException.MSG,
                err_code=HomeContextBuilderException.ERR_CODE,
                ex=HomeContextBuildRouteException(
                    msg=HomeContextBuildRouteException.MSG,
                    err_code=HomeContextBuildRouteException.ERR_CODE,
                )
            )
        )
        
    
