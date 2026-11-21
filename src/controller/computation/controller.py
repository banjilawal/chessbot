# src/controller/computation/controller.py

"""
Module: controller.computation.controller
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from controller import Controller

T = TypeVar('T')

class ComputationController(Controller, ABC, Generic[T]):
    pass