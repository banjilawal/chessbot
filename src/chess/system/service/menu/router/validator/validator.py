# src/chess/system/service/menu/route/validator/validator.py

"""
Module: chess.system.service.menu.route.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC

from chess.system import ServiceRoute, Validator


class ServiceRouteValidator(Validator[ServiceRoute], ABC):
    pass