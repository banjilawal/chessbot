# src/model/context/vector/model.py

"""
Module: model.context.vector.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from model import VectorContext


@dataclass
class VectorRegister:
    u: VectorContext
    v: VectorContext
