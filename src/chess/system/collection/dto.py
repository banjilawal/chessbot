# src/chess/system/collectiondto.py

"""
Module: chess.system.collection.dto
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC
from typing import Generic

from chess.system.utils import T


class DTO(ABC, Generic[T]):
    pass