# src/bootstrapper/searcher/bootstrapper.py

"""
Module: bootstrapper.searcher.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod

from bootstrapper import Bootstrapper
from artifcat.report import Report
from artifcat import AnalysisResult
from util import LoggingLevelRouter


class SearcherBootstrapper(Bootstrapper):
    DOMAIN = "BootStrap"
    PACAKGE = "Searcher"
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs, ) -> AnalysisResult[Report]:
        pass