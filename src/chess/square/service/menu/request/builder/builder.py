# src/chess/square/service/menu/request/builder/builder.py

"""
Module: chess.square.service.menu.request.builder.builder
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC

from chess.square import Builder, ServiceRequest


class ServiceRequestBuilder(Builder[ServiceRequest], ABC):
    pass