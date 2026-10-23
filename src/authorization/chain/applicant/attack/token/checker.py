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

    Responsibilities:
        1.  Checks that an applicant satisfies one of the Attack requirements.

    Attributes:
        
    Provides:
        -   def execute(self, request: AttackRequest) -> AttackDecision

    Super Class:
        AttackApplicantChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackRequest) -> AttackDecision:
        pass