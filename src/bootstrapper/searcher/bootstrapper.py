# src/carrier_validator/searcher/carrier_validator.py

"""
Module: carrier_validator.searcher.carrier_validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod

from bootstrapper import Bootstrapper
from report import Report
from result import AnalysisResult
from util import LoggingLevelRouter


class SearcherBootstrapper(Bootstrapper):
    DOMAIN = "BootStrap"
    PACAKGE = "Searcher"
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs, ) -> AnalysisResult[Report]:
        pass