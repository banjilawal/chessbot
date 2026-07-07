# src/permitter/permitter.py

"""
Module: permitter.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import abstractmethod

from permitter import Permitter
from report import PushApprovalReport
from request import PushRequest
from util import LoggingLevelRouter


class PushPermitter(Permitter):
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
        OperationPermitter
        
    Notes:
        An OperationApprovalReport should be in the success payload.
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def run(self, request: PushRequest,) -> PushApprovalReport:
        pass