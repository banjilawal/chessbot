# src/permitter/permitter.py

"""
Module: permitter.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from abc import ABC, abstractmethod

from bootstrapper import PrimingValidator
from report import OperationApprovalReport
from request import Request
from util import LoggingLevelRouter



class Permitter(ABC):
    """
    Role:
        -   Request Analyzer
        -   Rights Granter
        -   Consistency, Integrity Maintenance

    Responsibilities:
        1.  Evaluate if a candidate can be granted permission to run an operation.

    Attributes:
        priming_validator: PrimingValidator
        
    Provides:
        -   run(self, request: Request, *args, **kwargs) -> OperationApprovalReport

    Super Class:
        Permitter
    """
    _priming_validator: PrimingValidator
    
    def __init__(self, priming_validator: PrimingValidator):
        """
        Args:
            priming_validator: PrimingValidator
        """
        self._priming_validator = priming_validator
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def run(self, request: Request, *args, **kwargs) -> OperationApprovalReport:
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