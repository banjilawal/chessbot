# src/core/adjudicator/request/push/adjudicator.py

"""
Module: core.adjudicator.request.push.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from core import RequestAdjudicator

T = TypeVar("T", bound="Model")

class PushRequestAdjudicator(RequestAdjudicator, ABC, Generic[T]):
    pass