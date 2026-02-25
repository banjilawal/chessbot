# src/chess/system/service/menu/route/route.py

"""
Module: chess.system.service.menu.route.route
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from typing import List

from chess.system import ServiceOperation


class ServiceRoute:
    _operations: List[ServiceOperation]
    