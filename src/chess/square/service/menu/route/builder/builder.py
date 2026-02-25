# src/chess/square/service/menu/route/builder/builder.py

"""
Module: chess.square.service.menu.route.builder.builder
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC

from chess.square import Builder, ServiceRoute


class ServiceRouteBuilder(Builder[ServiceRoute], ABC):
    pass