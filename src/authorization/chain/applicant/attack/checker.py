# src/authorization/chain/applicant/attack/checker.py

"""
Module: authorization.chain.applicant.attack.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import AttackDecision
from authorization import ApplicantChecker
from domain import Actor
from exchange import AttackRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")


class AttackApplicantChecker(ApplicantChecker[AttackRequest], ABC, Generic[T]):
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