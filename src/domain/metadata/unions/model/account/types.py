# src/domain/metadata/unions/model/account/types.py

"""
Module: domain.metadata.unions.account.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import ModelTypeUnion, Account, AccountBlueprint
from transit import AccountCarrier

T = TypeVar("T", bound="Account")


class AccountTypeUnion(ModelTypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Account.

    Attributes:
        model: Type[T]
        carrier: Type[AccountCarrier[T]]
        blueprint: Type[AccountBlueprint[T]]

    Provides:

    Super Class:
        ModelTypeUnion
    """
    
    def __init__(
            self,
            model: Type[T],
            carrier: Type[AccountCarrier[T]],
            blueprint: Type[AccountBlueprint[T]],
    ):
        """
        Args:
            model: Type[T]
            carrier: Type[AccountCarrier[T]]
            blueprint: Type[AccountBlueprint[T]]
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)
    
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[AccountCarrier[T]]:
        return cast(Type[AccountCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[AccountBlueprint[T]]:
        return cast(Type[AccountBlueprint[T]], super().blueprint)