# src/core/adjudicator/request/push/core/adjudicator.py

"""
Module: core.adjudicator.request.push.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import TypeVar

from core.adjudicator import RequestAdjudicator

T = TypeVar("T", bound="Model")

class PushRequestAdjudicator(RequestAdjudicator):
    pass