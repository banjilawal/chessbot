# src/production/endpoint/validation/context/flag.py

"""
Module: production.endpoint.validation.context.flag
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from assurance import LayerToolkit
from domain import Context, ContextPrimeExtract
from transit import ContextCarrier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Context")

class ContextFlagValidator(ABC, Generic[T]):
    
    _toolkit: LayerToolkit
    
    def __init__(self, toolkit: LayerToolkit):
        self._toolkit = toolkit
        
    @property
    def toolkit(self) -> LayerToolkit:
        return self._toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
            prime_extract: ContextPrimeExtract[T],
    ) -> ValidationResult[ContextCarrier[T]]:
        pass