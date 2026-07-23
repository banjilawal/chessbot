# src/carrier_validator/operation/carrier_validator.py

"""
Module: carrier_validator.operation.carrier_validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from abc import abstractmethod

from bootstrapper.bootstrapper import Bootstrapper
from operation import Operation
from util import LoggingLevelRouter


class OperationBootstrapper(Bootstrapper[Operation]):
    PACAKGE = "Operation"
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs,) -> Result:
        pass