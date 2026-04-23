# src/model/query/py

"""
Module: model.query.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

from model import Context

T = TypeVar("T")

@dataclass
class Query(ABC, Generic[T]):
    """
    Role:
        -   Model
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  Platform primitive to build Query APIs

    Attributes:
        context: Context[T]

    Provides:

    Super Class:
    """
    context: Context[T]
    
    
