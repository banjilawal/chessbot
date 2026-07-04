# src/model/state/notification/model/state.py

"""
Module: model.state.notification.model
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
    