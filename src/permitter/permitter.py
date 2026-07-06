# src/permitter/permitter.py

"""
Module: permitter.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from report import OperationApprovalReport
from result import AnalysisResult
from util import LoggingLevelRouter

T = TypeVar("T")

class Permitter(ABC, Generic[T]):
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
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, requestor: T, *args, **kwargs,) -> AnalysisResult[OperationApprovalReport]:
        """
        Implement in TokenPermitter subclasses.
        Args:
            requestor: T
            *args:
            *kwargs:
        Returns:
            AnalysisResult
        Raises:
            PermitterException
        """
        pass