# src/model/report/relation/__init__.py

"""
Module: model.report.relation.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from typing import Optional


class RelationReport:
    _primary: Optional[Any]
    _satellite: Optional[Any]
    _exception: Optional[Exception]
    _status: Optional[RelationState]
    
    def __init__(
            self,
            primary: Optional[Any],
            satellite: Optional[Any],
            status: RelationState,
            exception: Optional[Exception],
    ):
        """INTERNAL: Use build methods instead of direct constructor."""
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
    def status(self) -> Optional[RelationState]:
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
                self._status == RelationState.NO_RELATION
        )
    
    @property
    def registration_does_not_exist(self) -> bool:
        return (
                self._exception is None and
                self._primary is None and
                self._satellite is not None and
                self._status == RelationState.REGISTRATION_NOT_SUBMITTED
        )
    
    @property
    def stale_link_exists(self) -> bool:
        return (
                self._exception is None and
                self._primary is not None and
                self._satellite is None and
                self._status == RelationState.STALE_LINK_NOT_PURGED
        )

    @property
    def fully_exists(self) -> bool:
        return (
                self._exception is None and
                self._primary is not None and
                self._satellite is not None and
                self._status == RelationState.BIDIRECTIONAL
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self._exception is not None and
                self._primary is None and
                self._satellite is None and
                self._status == (
                        RelationState.ANALYZER_FAILED or
                        RelationState.ANALYZER_TIMED_OUT
                )
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self._exception is not None and
                self._primary is None and
                self._satellite is None and
                self._status == (
                        RelationState.ANALYZER_FAILED or
                        RelationState.ANALYZER_TIMED_OUT
                )
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> RelationReport:
        return RelationReport(
            primary=None,
            satellite=None,
            exception=exception,
            status=RelationState.ANALYZER_FAILED,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> RelationReport:
        return RelationReport(
            primary=None,
            satellite=None,
            exception=exception,
            status=RelationState.ANALYZER_TIMED_OUT,
        )
    
    @classmethod
    def no_relation(cls) -> RelationReport[Any, Any]:
        return RelationReport(
            primary=None,
            satellite=None,
            exception=None,
            status=RelationState.NO_RELATION,
        )
    
    @classmethod
    def registration_missing(cls, satellite: Any) -> RelationReport:
        return RelationReport(
            primary=None,
            exception=None,
            satellite=satellite,
            status=RelationState.REGISTRATION_NOT_SUBMITTED,
        )
    
    @classmethod
    def stale_link(cls, primary: Any) -> RelationReport:
        return RelationReport(
            satellite=None,
            exception=None,
            primary=primary,
            status=RelationState.STALE_LINK_NOT_PURGED,
        )
    
    @classmethod
    def bidirectional(cls, primary: Any, satellite: Any) -> RelationReport:
        return RelationReport(
            exception=None,
            primary=primary,
            satellite=satellite,
            status=RelationState.BIDIRECTIONAL,
        )
        