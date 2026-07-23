# src/carrier_validator/carrier_validator.py

"""
Module: carrier_validator.carrier_validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from result import Result
from util import LoggingLevelRouter


class Bootstrapper(ABC):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs, ) -> Result:
        pass