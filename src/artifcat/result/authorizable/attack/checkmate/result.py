# src/artifact/result/authorizable/attack/checkmate/result.py

"""
Module: artfifact.result.authorizable.attack.checkmate.result.
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackResult, ResultState
from domain import CheckmateEncounter


class CheckmateResult(AttackResult[CheckmateEncounter]):
    """
    Role:
        - Data Transport
        - Error Transport

    Responsibilities:
        1.  Contains details of a CheckmateEncounter transaction.

    Attributes:
        payload: Optional[CheckmateEncounter]

    Provides:
        -   def success(payload: CheckmateEncounter) -> CheckmateResult

    Super Class:
        AttackResult
    """
    
    def __init__(
            self,
            state: ResultState,
            payload: Optional[CheckmateEncounter] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: resultState
            payload: Optional[CheckmateEncounter]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            payload=payload,
            exception=exception,
        )
        """INTERNAL: Use attack methods instead of direct constructor."""
    
    @property
    def payload(self) -> Optional[CheckmateEncounter]:
        return cast(CheckmateEncounter, super().payload)
    
    @classmethod
    def success(cls, payload: CheckmateEncounter) -> CheckmateResult:
        return cls(
            payload=payload,
            state=ResultState.SUCCESS,
        )