# src/bootstrapper/bootstrapper.py

"""
Module: bootstrapper.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from artifcat import Result
from util import LoggingLevelRouter


class Bootstrapper(ABC):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs, ) -> Result:
        pass