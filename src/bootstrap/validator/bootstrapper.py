# src/bootstrap/validator/bootstrapper.py

"""
Module: bootstrap.validator.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod

from bootstrap import Bootstrapper
from result import ValidationResult
from util import LoggingLevelRouter


class ValidatorBootstrapper(Bootstrapper):
    DOMAIN = "BootStrap"
    PACAKGE = "Validator"
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def validate(cls, *args, **kwargs, ) -> ValidationResult:
        pass