# src/report/relation/report.py

"""
Module: report.relation.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from report import RelationState, Report

@dataclass
class RelationReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Presents the results of testing if two entities have a bidirectional relationship.

    Attributes:
        primary: Optional[Any]
        satellite: Optional[Any]
        status: RelationState

        does_not_exist: bool
        registration_does_not_exist: bool
        stale_link_exists: bool
        fully_exists: bool

    Provides:
        -   def no_relation(cls) -> RelationReport:
        -   def registration_missing(cls, satellite: Any) -> RelationReport:
        -   def stale_link(cls, primary: Any) -> RelationReport:
        -   def bidirectional(cls, primary: Any, satellite: Any) -> RelationReport

    Super Class:
        Report
    """
    primary: Optional[Any]
    satellite: Optional[Any]
    status: Optional[RelationState]
        
    @property
    def primary(self) -> Optional[Any]:
        return self.primary
    
    @property
    def satellite(self) -> Optional[Any]:
        return self.satellite
    
    @property
    def status(self) -> Optional[RelationState]:
        return self.status
    
    @property
    def does_not_exist(self) -> bool:
        return (
                self.primary is None and
                self.satellite is None and
                self.status == RelationState.NO_RELATION
        )
    
    @property
    def registration_does_not_exist(self) -> bool:
        return (
                self.primary is None and
                self.satellite is not None and
                self.status == RelationState.REGISTRATION_NOT_SUBMITTED
        )
    
    @property
    def stale_link_exists(self) -> bool:
        return (
                self.primary is not None and
                self.satellite is None and
                self.status == RelationState.STALE_LINK_NOT_PURGED
        )

    @property
    def fully_exists(self) -> bool:
        return (
                self.primary is not None and
                self.satellite is not None and
                self.status == RelationState.BIDIRECTIONAL
        )
    
    @classmethod
    def no_relation(cls) -> RelationReport[Any, Any]:
        return RelationReport(
            primary=None,
            satellite=None,
            status=RelationState.NO_RELATION,
        )
    
    @classmethod
    def registration_missing(cls, satellite: Any) -> RelationReport:
        return RelationReport(
            primary=None,
            satellite=satellite,
            status=RelationState.REGISTRATION_NOT_SUBMITTED,
        )
    
    @classmethod
    def stale_link(cls, primary: Any) -> RelationReport:
        return RelationReport(
            satellite=None,
            primary=primary,
            status=RelationState.STALE_LINK_NOT_PURGED,
        )
    
    @classmethod
    def bidirectional(cls, primary: Any, satellite: Any) -> RelationReport:
        return RelationReport(
            primary=primary,
            satellite=satellite,
            status=RelationState.BIDIRECTIONAL,
        )
        