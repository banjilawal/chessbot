# src/chess/system/service/menu/operation/builder/builder.py

"""
Module: chess.system.service.menu.operation.builder.builder
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC

from chess.system import Builder, ServiceOperation


class ServiceOperationBuilder(Builder[ServiceOperation], ABC):
    pass