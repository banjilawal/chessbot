# src/authorization/authorizer/stack/search/authorizer.py

"""
Module: authorization.authorizer.stack.search.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import abstractmethod

from authorization.authorizer.crud.stack import OperationAuthorizer
from artifcat.report import SearchApprovalReport
from client.exchange import SearchAuthorizationRequest
from util import LoggingLevelRouter


class SearchAuthorizer(OperationAuthorizer):
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
    def execute(self, request: SearchAuthorizationRequest, ) -> SearchApprovalReport:
        pass