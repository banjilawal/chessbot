# src/chess/graph/node/status.py

"""
Module: chess.graph.node.status
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from enum import Enum, auto


class DiscoveryStatus(Enum):
    UNKNOWN = auto(),
    DISCOVERED = auto(),
    PROCESSED = auto(),