# src/domain/metadata/unions/cartesian/types.py

"""
Module: domain.metadata.unions.cartesian.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Blueprint, CartesianPoint, TypeUnion
from transit import EntityCarrier

T = TypeVar("T", bound="CartesianPoint")


class CartesianTypeUnion(TypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a CartesianPoint.

    Attributes:
        model: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[Blueprint[T]]

    Provides:

    Super Class:
        TypeUnion
    """
    pass