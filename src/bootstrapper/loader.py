# src/bootstrapper/loader.py

"""
Module: bootstrapper.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T")

class Loader(ABC, Generic[T]):
    pass