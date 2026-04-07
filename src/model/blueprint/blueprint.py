# src/model/blueprint/blueprint.py

"""
Module: model.blueprint.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T")

class Blueprint(ABC, Generic[T]):
    pass