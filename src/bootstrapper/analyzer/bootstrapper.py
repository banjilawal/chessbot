# src/bootstrapper/analyzer/bootstrapper.py

"""
Module: bootstrapper.analyzer.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod

from bootstrapper import Bootstrapper
from artifcat.report import Report
from artifcat.result import AnalysisResult
from util import LoggingLevelRouter


class AnalyzerBootstrapper(Bootstrapper):
    DOMAIN = "BootStrap"
    PACAKGE = "Analyzer"
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs, ) -> AnalysisResult[Report]:
        pass