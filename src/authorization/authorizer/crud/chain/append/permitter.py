# src/authorization/authorizer/chain/append/authorizer.py

"""
Module: authorization.authorizer.chain.append.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import abstractmethod

from authorization.authorizer.crud.chain import ChainOperationAuthorizer
from artifcat.report import AppendApprovalReport
from client.exchange import AppendRequest
from util import LoggingLevelRouter


class AppendAuthorizer(ChainOperationAuthorizer):
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
    def execute(self, request: AppendRequest, ) -> AppendApprovalReport:
        pass