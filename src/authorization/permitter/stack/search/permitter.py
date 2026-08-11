# src/authorization/permitter/stack/search/permitter.py

"""
Module: authorization.permitter.stack.search.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import abstractmethod

from authorization.permitter.stack import OperationPermitter
from report import SearchApprovalReport
from request import SearchRequest
from util import LoggingLevelRouter


class SearchPermitter(OperationPermitter):
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
        Permitter
    """
    def __init__(self):
        super().__init__()
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: SearchRequest, ) -> SearchApprovalReport:
        pass