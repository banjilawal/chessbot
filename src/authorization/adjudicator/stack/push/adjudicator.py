# src/authorization/adjudicator/stack/push/adjudicator.py

"""
Module: authorization.adjudicator.stack.push.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from authorization import RequestAdjudicator

T = TypeVar("T", bound="Model")

class PushRequestAdjudicator(RequestAdjudicator, ABC, Generic[T]):
    pass