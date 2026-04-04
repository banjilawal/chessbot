# src/geometry/span/spanner/validator.py

"""
Module: geometry.span.spanner.computer
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict

from math.span import CoordSpan
from system import ComputationResult, Compute


class Spanner(Compute[CoordSpan]):
    """
    """
    
    @classmethod
    def compute(cls, *args, **kwargs) -> ComputationResult[Dict[str, CoordSpan]]:
        pass
    