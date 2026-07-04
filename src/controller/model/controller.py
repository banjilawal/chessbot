# src/controller/model/controller.py

"""
Module: controller.model.controller
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, TypeVar

from controller import Controller

T = TypeVar('T')

class ModelController(Controller[T]):
    pass