# src/chess/system/service/request/builder/builder.py

"""
Module: chess.system.service.request.builder.builder
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

from abc import ABC

from chess.system import Builder, ServiceRequest


class ServiceRequestBuilder(Builder[ServiceRequest], ABC):
    pass