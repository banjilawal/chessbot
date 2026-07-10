# src/operand/state/query/py

"""
Module: operand.state.query.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

from operand import Context

T = TypeVar("T")

@dataclass
class Query(ABC, Generic[T]):
    """
    Role:
        -   Operand
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  Platform primitive to build Query APIs

    Attributes:
        context: Context[T]

    Provides:

    Super Class:
        Operand
    """
    context: Context[T]
    
    
