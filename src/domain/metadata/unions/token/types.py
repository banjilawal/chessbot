# src/domain/metadata/unions/token/types.py

"""
Module: domain.metadata.unions.token.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import Token, TypeUnion

T = TypeVar("T", bound="Token")

class TokenTypeUnion(TypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Token.

    Attributes:

    Provides:

    Super Class:
        TypeUnion
    """
    pass