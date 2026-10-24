# src/operation/attack/attacker.py

"""
Module: operation.attack.attacker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from artifcat import AttackResult
from domain import Encounter
from operation import Worker

T = TypeVar("T", bound="Encounter")

class Attacker(Worker[AttackResult], ABC, Generic[T]):
    
    def __init__(
            self,
            authorization_responder: Optional[AttackAuthorizationResponder] | None = None,
    ):
        """
        Args:
            authorization_responder: Optional[AttackAuthorizationResponder]
        """