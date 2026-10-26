# src/domain/metadata/nulls/context/account/group.py

"""
Module: domain.metadata.nulls.context.account.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import ContextNullGroup, Account
from err import (
    AccountContextBlueprintNullException, AccountContextCarrierNullException, AccountContextNullException
)

T = TypeVar("T", bound="Account")

class AccountContextNullGroup(ContextNullGroup[T], Generic[TContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Account's integrity cycle.

    Attributes:
        context: AccountContextNullException
        carrier: AccountContextCarrierNullException
        blueprint: AccountContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[AccountContextNullException] | None = None,
            carrier: Optional[AccountContextCarrierNullException] | None = None,
            blueprint: Optional[AccountContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[AccountContextNullException]
            carrier: Optional[AccountContextCarrierNullException]
            blueprint: Optional[AccountContextBlueprintNullException]
        """
        super().__init__(
            context = context or AccountContextNullException(),
            carrier = carrier or AccountContextCarrierNullException(),
            blueprint = blueprint or AccountContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> AccountContextNullException:
        return cast(AccountContextNullException, super().context)
    
    @property
    def carrier(self) -> AccountContextCarrierNullException:
        return cast(AccountContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> AccountContextBlueprintNullException:
        return cast(AccountContextBlueprintNullException, super().blueprint)