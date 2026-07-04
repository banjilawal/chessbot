# src/bootstrap/analyzer/bootstrapper.py

"""
Module: bootstrap.analyzer.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod

from analyzer import Analyzer
from bootstrap import Bootstrapper
from util import LoggingLevelRouter


class AnalyzerBootstrapper(Bootstrapper[Analyzer]):
    DOMAIN = "BootStrap"
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs, ) -> AnalysisResult[Report]:
        pass