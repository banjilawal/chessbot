# src/permitter/permitter.py

"""
Module: permitter.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from abc import ABC, abstractmethod

from report import OperationApprovalReport
from request import Request
from util import LoggingLevelRouter



class Permitter(ABC):
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
    def run(request: Request, *args, **kwargs) -> OperationApprovalReport:
        """
        Implement in TokenPermitter subclasses.
        Args:
            request: Request
            *args:
            *kwargs:
        Returns:
            AnalysisResult
        Raises:
            PermitterException
        """
        pass