# src/permitter/search/permitter.py

"""
Module: permitter.search.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import abstractmethod

from permitter import Permitter
from report import SearchApprovalReport
from request import SearchRequest
from util import LoggingLevelRouter


class SearchPermitter(Permitter):
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
    def run(self, request: SearchRequest,) -> SearchApprovalReport:
        pass