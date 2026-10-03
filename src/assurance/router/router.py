# src/assurance/router/router.py

"""
Module: assurance.router.router
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import Model

T = TypeVar("T", bound="Model")

class SubclassValidationRouter(ABC, Generic[T]):
    pass