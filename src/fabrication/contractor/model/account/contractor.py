# src/fabrication/contractor/model/account/contractor.py

"""
Module: fabrication.contractor.model.account.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import BuildResult
from domain import Account, AccountBlueprint
from fabrication import ModelBuildSubcontractor
from util import LoggingLevelRouter

T = TypeVar("T", bound="Account")

class AccountSubcontractor(ModelBuildSubcontractor[T], ABC, Generic[T]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a concrete Account.

    Attributes:

    Provides:
            -   def execute(blueprint: AccountBlueprint[T]) -> BuildResult[T]

    Super Class:
        ModelBuildContractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: AccountBlueprint[T]) -> BuildResult[T]:
        """
        Routes a AccountBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: AccountBlueprint[T]
        Returns:
            BuildResult[T]
        Raises:
            AccountSubcontractorException
        """
        pass