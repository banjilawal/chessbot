# src/transit/dispatcher/dispatcher.py

"""
Module: transit.dispatcher.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import Result

T = TypeVar("T", bound="Result")

class Dispatcher(ABC, Generic[T]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Direct jobs towards a worker then forward the results to clients.

    Attributes:

    Provides:

    Super Class:
        Dispatcher
    """
    pass
