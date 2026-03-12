# src/logic/span/spanner/computer.py

"""
Module: logic.span.spanner.computer
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict

from logic.span import CoordSpan
from logic.system import ComputationResult, Computer


class Spanner(Computer[CoordSpan]):
    """
    """
    
    @classmethod
    def compute(cls, *args, **kwargs) -> ComputationResult[Dict[str, CoordSpan]]:
        pass
    