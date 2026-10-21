# src/authorization/authorizer/stack/push/authorizer.py

"""
Module: authorization.authorizer.stack.push.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import abstractmethod

from authorization.authorizer.stack import OperationAuthorizer
from artifcat.report import PushApprovalReport
from client.exchange import TokenStackPushRequest
from util import LoggingLevelRouter


class StackPushAuthorizer(OperationAuthorizer):
    """
    Role:
        - Analysis Worker
        - Consistency, Integrity Maintenance

    Responsibilities:
        1.  Checks if an object satisfies the conditions to perform an operation.

    Attributes:

    Provides:
        -   def execute(cls, requestor: T, *args, **kwargs) -> AnalysisResult

    Super Class:
        Authorizer
    """
    def __init__(self):
        super().__init__()
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: TokenStackPushRequest, ) -> PushApprovalReport:
        pass