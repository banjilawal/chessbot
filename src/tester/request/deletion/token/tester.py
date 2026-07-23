# src/tester/request/deletion/token/tester.py

"""
Module: tester.request.deletion.token.tester
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


from __future__ import annotations

from typing import Any, Type, cast

from bootstrapper import DeletionPermitterBootstrapper, PrimingValidator
from err import TokenStackNullException
from microservice import IdentityService
from request import DeletionRequest
from result import MethodResultType, ValidationResult
from stack import TokenStackService
from tester import DeletionRequestTester
from util import LoggingLevelRouter


class TokenDeletionRequestTester(DeletionRequestTester):
    """
    Role:
        -   Helper
        -   Test Runner
        
    Responsibilities:
        1.  Check if the subject is a deletion that can be promoted.
        
    Attributes:
        identity_service: IdentityService
        priming_validator: PrimingValidator
        carrier_validator: DeletionPermitterBootstrapper
          
    Provides:
        -   def execute(self, subject: Any) -> ValidationResult:
            
    Super Class:
    """
    _identity_service: IdentityService
    _priming_validator: PrimingValidator
    _bootstrapper: DeletionPermitterBootstrapper
    
    def __init__(
            self,
            identity_service: IdentityService | None = IdentityService(),
            priming_validator: PrimingValidator | None = PrimingValidator(),
            bootstrapper: DeletionPermitterBootstrapper | None = DeletionPermitterBootstrapper(),
    ):
        """
        Args:
            identity_service: IdentityService
            priming_validator: PrimingValidator
            bootstrapper: DeletionPermitterBootstrapper
        """
        self._bootstrapper = bootstrapper
        self._identity_service = identity_service
        self._priming_validator = priming_validator
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult:
        """
        Verifies the subject is a promotable deletion.
        
        Action:
            1.  Send an exception chain in the ValidationResult if any of the following occur:
                    -   The subject is flagged unsafe.
                    -   The subject is not a free deletion.
                    -   The deletion has already been promoted.
                    -   Is not on its enemy's rank_row.
            2.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[DeletionToken]
        Raises:
            TokenStackDeletionTesterException
            PromoteInactiveDeletionException
            DeletionDoubleStackException
            DeletionStackRowException
            TypeError
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the DeletionRequest is not bootstrapped successfully.
        bootstrap = self._bootstrapper.execute(candidate)
        if bootstrap.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                TokenDeletionRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenDeletionRequestTesterException.MSG,
                    err_code=TokenDeletionRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=bootstrap.exception
                )
            )
        request = cast(DeletionRequest, bootstrap.payload)
        # handle the case that, the item is not a safe token.
        id_test = self._identity_service.validate_id(request.item_id)
        if id_test.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                TokenDeletionRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenDeletionRequestTesterException.MSG,
                    err_code=TokenDeletionRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=id_test.exception
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
                TokenDeletionRequestTesterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenDeletionRequestTesterException.MSG,
                    err_code=TokenDeletionRequestTesterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=stack_test.exception
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(request)