# src/operand/state/notification/operand/state.py

"""
Module: operand.state.notification.operand
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from event import Event


@dataclass
class Notification:
    id: int
    event: Event
    