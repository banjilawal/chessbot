# src/sensor/detector.py

"""
Module: sensor.detector.detector
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from sensor import Sensor

T = TypeVar("T", bound="StateModel")


class EnvironmentReporter(Sensor, ABC, Generic[T]):
    pass
