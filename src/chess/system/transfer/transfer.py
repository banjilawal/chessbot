# src/chess/system/transfer/transfer.py

"""
Module: chess.system.transfer.transfer
Author: Banji Lawal
Created: 2026-02-01
version: 1.0.0
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

S = TypeVar("S")
R = TypeVar("R")

from chess.system import LoggingLevelRouter
from chess.system.transfer import TransferResult

class Transfer(ABC, Generic[S, R]):
    """
    """
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def transfer(cls, sender: S, recipient: R) -> TransferResult[S, R]:
        pass