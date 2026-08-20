# src/status/state.py

"""
Module: status.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations
from enum import Enum, auto


class DiscoveryStatus(Enum):
    UNKNOWN = auto(),
    DISCOVERED = auto(),
    PROCESSED = auto(),