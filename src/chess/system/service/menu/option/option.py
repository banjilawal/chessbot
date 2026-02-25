# src/chess/system/service/menu/option/option.py

"""
Module: chess.system.service.menu.option.option
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system import LoggingLevelRouter, RelationReport, Service


S = TypeVar("S", binding=Service)


class MenuOption(ABC, Generic[S]):
    _label: str
    