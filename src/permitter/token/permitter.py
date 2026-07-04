# src/deletion/token/py

"""
Module: deletion.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod

from model import Token
from permitter import OperationPermitter
from result import AnalysisResult
from util import LoggingLevelRouter


class TokenPermitter(OperationPermitter):
    """
    Role:
        - Analysis Worker
        - Consistency, Integrity Maintenance

    Responsibilities:
        1.  Checks if a Token satisfies the conditions to perform an operation.

    Attributes:

    Provides:
        -   def execute(cls,token: Token, *args, **kwargs) -> AnalysisResult
        
    Super Class:
        OperationPermitter
    """
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, requestor: Token, *args, **kwargs) -> AnalysisResult:
        """
        Implement in TokenPermitter subclasses.
        Args:
            requestor: Token
            *args:
            *kwargs:
        Returns:
            AnalysisResult
        Raises:
            TokenPermitterException
        """
        pass
    