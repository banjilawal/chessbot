# src/logic/system/collection/dto.py

"""
Module: logic.system.collection.dto
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC
from typing import Generic

from logic.system.utils import T


class DTO(ABC, Generic[T]):
    pass