# src/production/endpoint/attractor/account/attractor.py

"""
Module: production.endpoint.attractor.account.attractor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import CollisionReport
from collection import AccountStack
from domain import Account
from environment import AccountCollisionDetector
from production import Attractor

from util import LoggingLevelRouter

T = TypeVar("T", bound="Account")

class AccountAttractor(Attractor[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Detect if an insert breaks Account collection's uniqueness
            constraint.

    Attributes:
        detector: CollisionDetector[T]

    Provides:
        -   def execute(target: T, particle_stream: Stack[T]) -> CollisionReport
        
    Super Class
        Attractor
    """
    
    def __init__(self, detector: Optional[AccountCollisionDetector] | None = None):
        """
        Args:
            detector: Optional[AccountCollisionDetector]
        """
        super().__init__(detector=detector or AccountCollisionDetector())
    
    @property
    def detector(self) -> AccountCollisionDetector:
        return cast(AccountCollisionDetector, super().detector)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, target: T, particle_stream: AccountStack) -> CollisionReport:
        """
        Assure the target will be unique in the Account collection.
        
        Action:
            1.  If the target shares an attribute-value supposed to be unique to the
                collection, send an exception chain in the report.
            2.  Otherwise, report that primary keys will be maintained.
        Args:
            target: T
            particle_stream: AccountStack
        Returns:
           CollisionReport
        Raises:
            AccountAttractorException
        """
        pass
    


        
        