# src/tester/request/push/tester.py

"""
Module: tester.request.push.tester
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import TypeVar

from tester import RequestTester

T = TypeVar("T", bound="Model")

class PushRequestTester(RequestTester):
    pass