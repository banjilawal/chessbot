# src/model/status/state.py

"""
Module: model.status.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from enum import Enum, auto


class DiscoveryStatus(Enum):
    UNKNOWN = auto(),
    DISCOVERED = auto(),
    PROCESSED = auto(),