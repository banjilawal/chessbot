# src/tester/stack/token/search/tester.py

"""
Module: tester.stack.token.search.tester
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from typing import Any, Type, cast

from bootstrapper import PrimingValidator, SearchPermitterBootstrapper
from err import TokenSearchRequestTesterException, TokenStackNullException
from request import SearchRequest
from result import MethodResultType, ValidationResult
from stack import TokenStackService
from util import LoggingLevelRouter
from validator import TokenContextValidator


class TokenSearchRequestTester:
    """
    Role:
        -   Helper
        -   Test Runner
        
    Responsibilities:
        1.  Check if the subject is a search that can be promoted.
        
    Attributes:
        item_validator: TokenContextValidator
        priming_validator: PrimingValidator
        bootstrapper: SearchPermitterBootstrapper
          
    Provides:
        -   def execute(self, subject: Any) -> ValidationResult:
            
    Super Class:
    """
    _item_validator: TokenContextValidator
    _priming_validator: PrimingValidator
    _bootstrapper: SearchPermitterBootstrapper
    
    def __init__(
            self,
            item_validator: TokenContextValidator | None = TokenContextValidator(),
            priming_validator: PrimingValidator | None = PrimingValidator(),
            bootstrapper: SearchPermitterBootstrapper | None = SearchPermitterBootstrapper(),
    ):
        """
        Args:
            item_validator: TokenContextValidator
            priming_validator: PrimingValidator
            bootstrapper: SearchPermitterBootstrapper
        """
        self._bootstrapper = bootstrapper
        self._item_validator = item_validator
        self._priming_validator = priming_validator
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult:
        """
        Verifies the subject is a promotable search.
        
        Action:
            1.  Send an exception chain in the ValidationResult if any of the following occur:
                    -   The subject is flagged unsafe.
                    -   The subject is not a free search.
                    -   The search has already been promoted.
                    -   Is not on its enemy's rank_row.
            2.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[SearchToken]
        Raises:
            TokenStackSearchTesterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the SearchRequest is not bootstrapped successfully.
        bootstrap = self._bootstrapper.bootstrap_request(candidate)
        if bootstrap.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                TokenSearchRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenSearchRequestTesterException.MSG,
                    err_code=TokenSearchRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=bootstrap.exception
                )
            )
        request = cast(SearchRequest, bootstrap.payload)
        # handle the case that, the item is not a safe token.
        context_test = self._item_validator.execute(request.item)
        if context_test.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                TokenSearchRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenSearchRequestTesterException.MSG,
                    err_code=TokenSearchRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=context_test.exception
                )
            )
        # Handle the case that, the request contains a malformed stack.
        stack_test = self._priming_validator.execute(
            candidate=request.stack,
            target_model=Type[TokenStackService],
            null_exception=TokenStackNullException()
        )
        # Send the exception chain in the permission denial.
        if stack_test.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                TokenSearchRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenSearchRequestTesterException.MSG,
                    err_code=TokenSearchRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=stack_test.exception
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(request)