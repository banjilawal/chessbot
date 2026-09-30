# src/domain/metadata/nulls/model/account/group.py

"""
Module: domain.metadata.nulls.model.account.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import ModelNullGroup, Account
from err import (
    AccountBlueprintNullException, AccountCarrierNullException, AccountNullException
)

T = TypeVar("T", bound="Account")

class AccountNullGroup(ModelNullGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Account's integrity cycle.

    Attributes:
        model: AccountNullException
        carrier: AccountCarrierNullException
        blueprint: AccountBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[AccountNullException] | None = None,
            carrier: Optional[AccountCarrierNullException] | None = None,
            blueprint: Optional[AccountBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[AccountNullException]
            carrier: Optional[AccountCarrierNullException]
            blueprint: Optional[AccountBlueprintNullException]
        """
        super().__init__(
            model = model or AccountNullException(),
            carrier = carrier or AccountCarrierNullException(),
            blueprint = blueprint or AccountBlueprintNullException(),
        )
        
    @property
    def model(self) -> AccountNullException:
        return cast(AccountNullException, super().model)
    
    @property
    def carrier(self) -> AccountCarrierNullException:
        return cast(AccountCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> AccountBlueprintNullException:
        return cast(AccountBlueprintNullException, super().blueprint)