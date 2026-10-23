# src/authorization/authorizer/chain/remove/authorizer.py

"""
Module: authorization.authorizer.chain.remove.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import abstractmethod
from typing import Type

from err import RemoveRequestNullException, RemoveperAuthorizerException
from authorization.authorizer.crud.chain import ChainOperationAuthorizer
from artifcat.report import RemoveApprovalReport
from client.exchange import RemoveRequest
from artifcat import ValidationResult
from util import LoggingLevelRouter


class RemoveAuthorizer(ChainOperationAuthorizer):
    """
    Role:
        - Request Analyzer
        - Rights Granter
        - Consistency, Integrity Maintenance

    Responsibilities:
        1.  Evaluate if a chain removeping request can be granted.

    Attributes:
        priming_validator: PrimingValidator

    Provides:
        - run(self, request: RemoveRequest,) -> RemoveApprovalReport:

    Super Class:
        Authorizer
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: RemoveRequest, ) -> RemoveApprovalReport:
        pass
    
    @LoggingLevelRouter.monitor
    def bootstrap_request(self, request) -> ValidationResult:
        """
        Evaluate a pawn promotion request.

        Action:
            1.  Send an exception chain in the ValidationResult if the request is either
                    - Null
                    - Not a RemoveRequest.
            2.  Otherwise, send the success
        Args:
            request
        Returns:
            ValidationResult
        Raises:
            RemoveperAuthorizerException
        """
        method = f"{self.__class__.__name__}.bootstrap_request"
        
        # Handle the case that the request is malformed
        validation_result = self.priming_validator.execute(
            candidate=request,
            target_model=Type[RemoveRequest],
            null_exception=RemoveRequestNullException()
        )
        if validation_result.is_failure:
            # Send the exception chain in the ValidationResult.
            return ValidationResult.failure(
                RemoveperAuthorizerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RemoveperAuthorizerException.MSG,
                    err_code=RemoveperAuthorizerException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        return ValidationResult.success(request)