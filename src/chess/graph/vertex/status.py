# src/chess/graph/square/status.py

"""
Module: chess.graph.square.status
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from enum import Enum, auto


class DiscoveryStatus(Enum):
    UNKNOWN = auto(),
    DISCOVERED = auto(),
    PROCESSED = auto()