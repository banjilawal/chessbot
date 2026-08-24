# src/assurance/checker/search/stack/checker.py

"""
Module: assurance.checker.search.stack.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

import config.setting.board.dimension.config
from artifcat import ValidationResult
from assurance import StackContextChecker, CoordValidationBundle
from domain import CoordSearchContext
from err import CoordContextCheckerException, ZeroContextFlagsException
from util import LoggingLevelRouter


class CoordContextChecker(StackContextChecker[CoordSearchContext]):
    """
    Role
        -   Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null CoordSearchContext.
        2.  Run safety checks on any CoordSearchContext attributes that are enabled.

    Attributes:
        bundle: CoordValidationBundle

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[CoordSearchContext]:

    Super Class:
        StackSearchContextChecker
    """
    
    def __init__(self, bundle: Optional[CoordValidationBundle] | None = None,):
        super().__init__(bundle=bundle or CoordValidationBundle())
        
    @property
    def bundle(self) -> CoordValidationBundle:
        return cast(CoordValidationBundle, super().bundle)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[CoordSearchContext]:
        """
        Certify a candidate is a CoordSearchContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate is not a CoordSearchContext.
                    -   The wrong number of search attributes is enabled.
                    -   An enabled search attribute fails a safety check.
            2.  Otherwise, send a TokeSearchContext in the success result.
        Args:
            candidate, Any
        Returns:
            ValidationResult[CoordSearchContext]
        Raises:
            CoordContextCheckerException
        """
        method = f"{self.__class__.__name__}.execute"

        
        # Handle the case that, the validator is not primed.
        priming_result = self.bundle.priming_validator.execute(
            candidate=candidate,
            target_model=self.bundle.types.search_context,
            null_exception=self.bundle.nulls.search_context,
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordContextCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordContextCheckerException.MSG,
                    err_code=CoordContextCheckerException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into SquareContext for routing attribute testing. ---#
        context = cast(CoordSearchContext, candidate)
        
        # Handle the case that none of the filters are enabled.
        if context.no_active_filters:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordContextCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordContextCheckerException.MSG,
                    err_code=CoordContextCheckerException.ERR_CODE,
                    ex=ZeroContextFlagsException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ZeroContextFlagsException.MSG,
                        err_code=ZeroContextFlagsException.ERR_CODE,
                    )
                )
            )        
        # Certification whichever attribute is enabled.
        for attribute in [context.row, context.column]:
            validation = self.bundle.number_validator.execute(
                candidate=attribute,
                floor=0,
                ceiling=config.setting.board.dimension.config.board_size - 1,
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    CoordContextCheckerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordContextCheckerException.MSG,
                        err_code=CoordContextCheckerException.ERR_CODE,
                        ex=validation.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(context)
        
    
    
