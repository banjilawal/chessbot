# src/artifact/result/authorizable/attack/kill/result.py

"""
Module: artfifact.result.authorizable.attack.kill.result.
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackResult, ResultState
from domain import KillEncounter


class KillResult(AttackResult[KillEncounter]):
    """
    Role:
        - Data Transport
        - Error Transport

    Responsibilities:
        1.  Contains details of a KillEncounter transaction.

    Attributes:
        payload: Optional[KillEncounter]

    Provides:
        -   def success(payload: KillEncounter) -> KillResult

    Super Class:
        AttackResult
    """
    
    def __init__(
            self,
            state: ResultState,
            payload: Optional[KillEncounter] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: resultState
            payload: Optional[KillEncounter]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            payload=payload,
            exception=exception,
        )
        """INTERNAL: Use attack methods instead of direct constructor."""
    
    @property
    def payload(self) -> Optional[KillEncounter]:
        return cast(KillEncounter, super().payload)
        
    @classmethod
    def success(cls, payload: KillEncounter) -> KillResult:
        return cls(
            payload=payload,
            state=ResultState.SUCCESS,
        )