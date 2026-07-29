# src/builder/pattern/builder/pattern.py

"""
Module: builder.pattern.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from builder import Builder

T = TypeVar("T", bound="Signature")

class PatternBuilder(Builder, ABC, Generic[T]):
    pass