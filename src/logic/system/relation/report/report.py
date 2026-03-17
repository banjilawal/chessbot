# src/logic/system/relation/report/report.py

"""
Module: logic.system.relation.report.report
Author: Banji Lawal
Created: 2025-12-28
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

from logic.system import RelationStatus


class RelationReport:
    _primary: Optional[Any]
    _satellite: Optional[Any]
    _exception: Optional[Exception]
    _status: Optional[RelationStatus]
    
    def __init__(
            self,
            primary: Optional[Any],
            satellite: Optional[Any],
            status: RelationStatus,
            exception: Optional[Exception],
    ):
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "RelationReport.__init__"
        self._primary = primary
        self._satellite = satellite
        self._relation_status = status
        self._exception = exception
        
    @property
    def primary(self) -> Optional[Any]:
        return self._primary
    
    @property
    def satellite(self) -> Optional[Any]:
        return self._satellite
    
    @property
    def status(self) -> Optional[RelationStatus]:
        return self._status
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def does_not_exist(self) -> bool:
        return (
                self._exception is None and
                self._primary is None and
                self._satellite is None and
                self._status == RelationStatus.NO_RELATION
        )
    
    @property
    def registration_does_not_exist(self) -> bool:
        return (
                self._exception is None and
                self._primary is None and
                self._satellite is not None and
                self._status == RelationStatus.REGISTRATION_NOT_SUBMITTED
        )
    
    @property
    def stale_link_exists(self) -> bool:
        return (
                self._exception is None and
                self._primary is not None and
                self._satellite is None and
                self._status == RelationStatus.STALE_LINK_NOT_PURGED
        )

    @property
    def fully_exists(self) -> bool:
        return (
                self._exception is None and
                self._primary is not None and
                self._satellite is not None and
                self._status == RelationStatus.BIDIRECTIONAL
        )
    
    @property
    def is_analyzer_failure(self) -> bool:
        return (
                self._exception is not None and
                self._primary is None and
                self._satellite is None and
                self._status == (
                        RelationStatus.ANALYZER_FAILED or
                        RelationStatus.ANALYZER_TIMED_OUT
                )
        )
    
    @property
    def is_analyzer_timed_out(self) -> bool:
        return (
                self._exception is not None and
                self._primary is None and
                self._satellite is None and
                self._status == (
                        RelationStatus.ANALYZER_FAILED or
                        RelationStatus.ANALYZER_TIMED_OUT
                )
        )
    
    @classmethod
    def analyzer_failure(cls, exception: Exception) -> RelationReport:
        return RelationReport(
            primary=None,
            satellite=None,
            exception=exception,
            status=RelationStatus.ANALYZER_FAILED,
        )
    
    @classmethod
    def analyzer_timed_out(cls, exception: Exception) -> RelationReport:
        return RelationReport(
            primary=None,
            satellite=None,
            exception=exception,
            status=RelationStatus.ANALYZER_TIMED_OUT,
        )
    
    @classmethod
    def no_relation(cls) -> RelationReport[Any, Any]:
        return RelationReport(
            primary=None,
            satellite=None,
            exception=None,
            status=RelationStatus.NO_RELATION,
        )
    
    @classmethod
    def registration_missing(cls, satellite: Any) -> RelationReport:
        return RelationReport(
            primary=None,
            exception=None,
            satellite=satellite,
            status=RelationStatus.REGISTRATION_NOT_SUBMITTED,
        )
    
    @classmethod
    def stale_link(cls, primary: Any) -> RelationReport:
        return RelationReport(
            satellite=None,
            exception=None,
            primary=primary,
            status=RelationStatus.STALE_LINK_NOT_PURGED,
        )
    
    @classmethod
    def bidirectional(cls, primary: Any, satellite: Any) -> RelationReport:
        return RelationReport(
            exception=None,
            primary=primary,
            satellite=satellite,
            status=RelationStatus.BIDIRECTIONAL,
        )
        