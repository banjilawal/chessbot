# src/controller/chain/controller.py

"""
Module: controller.chain.controller
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from collection import Chain
from controller import Controller

T = TypeVar("T", bound="Chain")

class ChainController(Controller[T], ABC, Generic[T]):
    _chain: T
    _adder: T
    _remover: T
    _trimmer: T
    _searcher: T
    