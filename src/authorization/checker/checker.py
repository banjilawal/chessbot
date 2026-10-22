# src/authorization/checker/checker.py

"""
Module: authorization.checker.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T")

class Checker(ABC, Generic[T]):
    pass