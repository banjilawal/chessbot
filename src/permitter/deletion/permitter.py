# src/permitter/deletion/permitter.py

"""
Module: permitter.deletion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import abstractmethod

from permitter import Permitter
from report import DeletionApprovalReport, PushApprovalReport
from request import DeletionRequest, PushRequest
from util import LoggingLevelRouter


class DeleterPermitter(Permitter):
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
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def run(self, request: DeletionRequest,) -> DeletionApprovalReport:
        pass