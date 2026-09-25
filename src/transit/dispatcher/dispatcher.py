# src/transit/dispatcher/dispatcher.py

"""
Module: transit.dispatcher.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from util import LoggingLevelRouter


class Dispatcher(ABC):
    """
    Role
        -   Director

    Responsibilities:
        1.  Forward client jobs to a worker.
        2.  Send the worker's product back to the caller.

    Attributes:

    Provides:

    Super Class:
        Dispatcher
    """
    pass
