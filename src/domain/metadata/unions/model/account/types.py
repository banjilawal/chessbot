# src/domain/metadata/unions/model/account/types.py

"""
Module: domain.metadata.unions.account.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from domain import ModelTypeUnion, Account, AccountBlueprint
from transit import AccountCarrier

T = TypeVar("T", bound="Account")


class AccountTypeUnion(ModelTypeUnion[T], Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Account.

    Attributes:
        model: Type[Account]
        carrier: Type[AccountCarrier]
        blueprint: Type[AccountBlueprint]

    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[T]] | None = None,
            carrier: Optional[Type[AccountCarrier[T]]] | None = None,
            blueprint: Optional[Type[AccountBlueprint[T]]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[T]]
            carrier: Optional[Type[AccountCarrier[T]]]
            blueprint: Optional[Type[AccountBlueprint[T]]]
        """
        super().__init__(
            model=model or Account,
            carrier=carrier or AccountCarrier,
            blueprint=blueprint or AccountBlueprint,
        )
    
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[AccountCarrier[T]]:
        return cast(Type[AccountCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[AccountBlueprint[T]]:
        return cast(Type[AccountBlueprint[T]], super().blueprint)