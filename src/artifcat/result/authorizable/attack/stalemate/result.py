# src/artifact/result/authorizable/attack/stalemate/result.py

"""
Module: artfifact.result.authorizable.attack.stalemate.result.
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackResult, ResultState
from domain import StalemateEncounter


class StalemateResult(AttackResult[StalemateEncounter]):
    """
    Role:
        - Data Transport
        - Error Transport

    Responsibilities:
        1.  Contains details of a StalemateEncounter transaction.

    Attributes:
        payload: Optional[StalemateEncounter]
        
    Provides:
        -   def success(payload: StalemateEncounter) -> StalemateResult

    Super Class:
        AttackResult
    """
    
    def __init__(
            self,
            state: ResultState,
            payload: Optional[StalemateEncounter] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: resultState
            payload: Optional[StalemateEncounter]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            payload=payload,
            exception=exception,
        )
        """INTERNAL: Use attack methods instead of direct constructor."""
    
    @property
    def payload(self) -> Optional[StalemateEncounter]:
        return cast(StalemateEncounter, super().payload)
    
    @classmethod
    def success(cls, payload: StalemateEncounter) -> StalemateResult:
        return cls(
            payload=payload,
            state=ResultState.SUCCESS,
        )