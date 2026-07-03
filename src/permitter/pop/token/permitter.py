# src/pop/token/py

"""
Module: pop.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import PoppingEmptyTokenStackException, TokenPopPermitterException, TokenStackNullException
from report import PopApproval
from result import AnalysisResult, MethodResultType
from stack import TokenStackService
from util import LoggingLevelRouter
from validation import PrimingValidator


class TokenPopPermitter:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a pop.

    Attributes:

    Provides:
        -   execute(
                    cls,
                    token_stack: TokenStackService,
                    validation_primer: ValidationPrimer
            ) -> AnalysisResult

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            stack: TokenStackService,
            validation_primer: PrimingValidator | None = None,
    ) -> AnalysisResult:
        """
        Action:
            1.  Return a failure result containing an exception chain if either:
                    -   stack is not valid.
            2.  Send a pop denial if the TokenStack is empty. Otherwise, approve the
                pop.
        Args:
            stack: TokenStackService
            validation_primer: ValidationPrimer
        Returns:
            AnalysisResult
        Raises:
            TokenPopPermitterException
            PoppingEmptyTokenStackException
        """
        method =  f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if validation_primer is None:
            validation_primer = PrimingValidator()

        stack_validation_result = validation_primer.validate(
            candidate=stack,
            target_model=TokenStackService,
            null_exception=TokenStackNullException()
        )
        if stack_validation_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                TokenPopPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPopPermitterException.MSG,
                    err_code=TokenPopPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=stack_validation_result.exception,
                )
            )
        if stack.is_empty:
            # Return the exception chain on failure
            return AnalysisResult.completed(
                PopApproval.deny(
                    exception=TokenPopPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenPopPermitterException.MSG,
                        err_code=TokenPopPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=PoppingEmptyTokenStackException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=PoppingEmptyTokenStackException.MSG,
                            err_code=PoppingEmptyTokenStackException.ERR_CODE,
                        ),
                    )
                )
            )
        # --- Integrity and performance tests are passed. ---#
        return AnalysisResult.completed(PopApproval.approve(stack=stack))

    