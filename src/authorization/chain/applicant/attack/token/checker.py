# src/authorization/chain/applicant/attack/token/checker.py

"""
Module: authorization.chain.applicant.attack.token.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from artifcat import AttackDecision
from authorization import AttackApplicantChecker
from domain import Token
from exchange import AttackRequest
from util import LoggingLevelRouter


class AttackTokenChecker(AttackApplicantChecker[Token], ABC):
    """
    Role:
        -   Authorization
        -   Interface

    Responsibilities:
        1.  Interface for checking a Token attribute satisfies Attack requirements.

    Attributes:

    Provides:
        -   def execute(request: AttackRequest) -> AttackDecision

    Super Class:
        AttackApplicantChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackRequest) -> AttackDecision:
        """
        Decide if a Token can be granted permission to launch an Attack.
        Args:
            request: AttackRequest
        Returns:
           AttackDecision
        Raises:
          AttackTokenCheckerException
        """
        pass
