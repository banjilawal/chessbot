# src/collection/stack//model/collection.py

"""
Module: collection.stack.model.collection
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from collection import Stack
from domain import Model

T = TypeVar("T", bound="Model")


class ModelStack(Stack, ABC, Generic[T]):
    """
    Role:
        -   Collection

    Responsibilities:
        1.  Stack of unique Model objects.

    Attributes:
        items: List[T]
 
    Provides:
    
    Super Class:
        Stack
    """