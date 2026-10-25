# src/artifact/result/authorizable/attack/warning/result.py

"""
Module: artfifact.result.authorizable.attack.warning.result.
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackResult, ResultState
from domain import EncounterWarning


class WarningResult(AttackResult[EncounterWarning]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Contains details of an EncounterWarning transaction.


    Attributes:
        payload: Optional[EncounterWarning]

    Provides:
        -   def success(payload: EncounterWarning) -> WarningResult

    Super Class:
        AttackResult
    """
    
    def __init__(
            self,
            state: ResultState,
            payload: Optional[EncounterWarning] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: resultState
            payload: Optional[EncounterWarning]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            payload=payload,
            exception=exception
        )

    @property
    def payload(self) -> Optional[EncounterWarning]:
        return cast(EncounterWarning, super().payload)
    
    @property
    def is_success(self) -> bool:
        return super().is_success and isinstance(self.payload, EncounterWarning)
    
    @classmethod
    def success(cls, payload: EncounterWarning) -> WarningResult:
        return cls(payload=payload, state=ResultState.SUCCESS)