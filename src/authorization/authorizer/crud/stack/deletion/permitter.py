# src/authorization/authorizer/stack/deletion/authorizer.py

"""
Module: authorization.authorizer.stack.deletion.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import abstractmethod
from typing import Type

from err import DdeletionAuthorizationRequestNullException, DeleteAuthorizerException
from authorization.authorizer.crud.stack import OperationAuthorizer
from artifcat.report import DeletionApprovalReport
from client.exchange import CollectionDdeletionAuthorizationRequest
from artifcat import ValidationResult
from util import LoggingLevelRouter


class DeleterAuthorizer(OperationAuthorizer):
    """
    Role:
        - Request Analyzer
        - Rights Granter
        - Consistency, Integrity Maintenance

    Responsibilities:
        1.  Evaluate if permission to remove a stack member can be granted.

    Attributes:

    Provides:
        - run(self, request: DdeletionAuthorizationRequest,) -> DeletionApprovalReport:

    Super Class:
        Authorizer
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: CollectionDdeletionAuthorizationRequest, ) -> DeletionApprovalReport:
        pass
    
    @LoggingLevelRouter.monitor
    def bootstrap_request(self, request) -> ValidationResult:
        """
        Evaluate a pawn promotion request.

        Action:
            1.  Send an exception chain in the ValidationResult if the request is either
                    - Null
                    - Not a PopRequest.
            2.  Otherwise, send the success
        Args:
            request
        Returns:
            ValidationResult
        Raises:
            DeleterAuthorizerException
        """
        method = f"{self.__class__.__name__}.bootstrap_request"
        
        # Handle the case that the request is malformed
        validation_result = self.priming_validator.execute(
            job=request,
            target_model=Type[CollectionDdeletionAuthorizationRequest],
            null_exception=DdeletionAuthorizationRequestNullException()
        )
        if validation_result.is_failure:
            # Send the exception chain in the ValidationResult.
            return ValidationResult.failure(
                DeleteAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DeleteAuthorizerException.MSG,
                    err_code=DeleteAuthorizerException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        return ValidationResult.success(request)