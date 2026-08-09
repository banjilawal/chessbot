# src/sensor/detector.py

"""
Module: sensor.detector.detector
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import TypeVar

from model import Token
from sensor import EnvironmentReporter

T = TypeVar("T", bound="StateModel")


class TokenEnvironmentReporter(EnvironmentReporter[Token], ABC):
    pass
