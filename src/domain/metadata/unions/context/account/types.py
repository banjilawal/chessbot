# src/domain/metadata/unions/context/account/types.py

"""
Module: domain.metadata.unions.context.account.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar, cast

from domain import ContextTypeUnion, Account, AccountContextBlueprint
from transit import AccountContextCarrier

T = TypeVar("T", bound="Account")


class AccountContextTypeUnion(ContextTypeUnion[TContext], Generic[TContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Account.

    Attributes:
        model: Type[AccountContext]
        carrier: Type[AccountContextCarrier]
        blueprint: Type[AccountContextBlueprint]

    Provides:

    Super Class:
        ContextTypeUnion
    """
    
    def __init__(
            self,
            model: Optional[Type[TContext]] | None = None,
            carrier: Optional[Type[AccountContextCarrier[TContext]]Context] | None = None,
            blueprint: Optional[Type[AccountContextBlueprint[TContext]]Context] | None = None,
    ):
        """
        Args:
            model: Optional[Type[TContext]]
            carrier: Optional[Type[AccountContextCarrier[TContext]]Context]
            blueprint: Optional[Type[AccountContextBlueprint[TContext]]Context]
        """
        super().__init__(
            model=model or AccountContext, 
            carrier=carrier or AccountContextCarrier,
            blueprint=blueprint or AccountContextBlueprint,
        )
    
    @property
    def model(self) -> Type[TContext]:
        return cast(Type[TContext], super().model)
    
    @property
    def carrier(self) -> Type[AccountContextCarrier[TContext]]:
        return cast(Type[AccountContextCarrier[TContext]], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[AccountContextBlueprint[TContext]]:
        return cast(Type[AccountContextBlueprint[TContext]], super().contextBlueprint)