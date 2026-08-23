# src/authorization/adjudicator/stack/search/token/adjudicator.py

"""
Module: authorization.adjudicator.stack.search.token.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Any, Type, cast

from priming_validator import PrimingValidator, SearchRequestPriming_Validator
from err import TokenSearchRequestAdjudicatorException, TokenStackNullException
from domain.exchange.request import SearchRequest
from artifcat.result import MethodResultType, ValidationResult
from collection.stack import TokenStackService
from authorization.adjudicator import SearchRequestAdjudicator
from util import LoggingLevelRouter
from assurance.validator import TokenContextValidator


class TokenSearchRequestAdjudicator(SearchRequestAdjudicator):
    """
    Role:
        -   Helper
        -   Test Runner
        
    Responsibilities:
        1.  Check if the subject is a search that can be promoted.
        
    Attributes:
        item_validator: TokenContextValidator
        priming_validator: PrimingValidator
        carrier_validator: SearchPermitterPriming_Validator
          
    Provides:
        -   def execute(self, subject: Any) -> ValidationResult:
            
    Super Class:
    """
    _item_validator: TokenContextValidator
    _priming_validator: PrimingValidator
    _priming_validator: SearchRequestPriming_Validator
    
    def __init__(
            self,
            item_validator: TokenContextValidator | None = TokenContextValidator(),
            priming_validator: PrimingValidator | None = PrimingValidator(),
            priming_validator: SearchRequestPriming_Validator | None = SearchRequestPriming_Validator(),
    ):
        """
        Args:
            item_validator: TokenContextValidator
            priming_validator: PrimingValidator
            priming_validator: SearchPermitterPriming_Validator
        """
        self._priming_validator = priming_validator
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
            TokenStackSearchAdjudicatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the SearchRequest is not bootstrapped successfully.
        bootstrap = self._priming_validator.execute(candidate)
        if bootstrap.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                TokenSearchRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenSearchRequestAdjudicatorException.MSG,
                    err_code=TokenSearchRequestAdjudicatorException.ERR_CODE,
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
                TokenSearchRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenSearchRequestAdjudicatorException.MSG,
                    err_code=TokenSearchRequestAdjudicatorException.ERR_CODE,
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
                TokenSearchRequestAdjudicatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenSearchRequestAdjudicatorException.MSG,
                    err_code=TokenSearchRequestAdjudicatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=stack_test.exception
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(request)