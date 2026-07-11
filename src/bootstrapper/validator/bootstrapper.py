# src/bootstrapper/validator/bootstrapper.py

"""
Module: bootstrapper.validator.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod

from bootstrapper import Bootstrapper
from result import ValidationResult
from util import LoggingLevelRouter


class ValidatorBootstrapper(Bootstrapper):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs, ) -> ValidationResult:
        pass