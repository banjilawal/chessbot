# src/chess/system/collection/operation/computation/state/__init__.py

"""
Module: chess.system.collection.operation.computation.state.__init__
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

from enum import auto, Enum


class ComputationResultEnum(Enum):
    """
    """
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),