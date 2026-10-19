# src/artifact/decision/permission.py

"""
Module: artfifact.decision.permission
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class Permission(Enum):
    GRANTED = auto(),
    DENIED = auto(),
    TIMED_OUT = auto(),