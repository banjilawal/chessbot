# src/chess/square/service/menu/route/validator/validator.py

"""
Module: chess.square.service.menu.route.validator.validator
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC

from chess.square import ServiceRoute, Validator


class ServiceRouteValidator(Validator[ServiceRoute], ABC):
    pass