# src/authorization/authorizer/chain/search/authorizer.py

"""
Module: authorization.authorizer.chain.search.authorizer
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import abstractmethod

from authorization.authorizer.chain import ChainOperationAuthorizer
from artifcat.report import SearchApprovalReport
from client.exchange import SearchRequest
from util import LoggingLevelRouter


class SearchAuthorizer(ChainOperationAuthorizer):
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
    def execute(self, request: SearchRequest, ) -> SearchApprovalReport:
        pass