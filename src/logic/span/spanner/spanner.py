# src/logic/span/spanner/computer.py

"""
Module: logic.span.spanner.computer
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict

from logic.span import Span
from logic.system import ComputationResult, Computer


class Spanner(Computer[Span]):
    """
    """
    
    @classmethod
    def compute(cls, *args, **kwargs) -> ComputationResult[Dict[str, Span]]:
        pass
    